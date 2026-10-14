import asyncio
import json
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.async_dispatcher import SemaphoreDispatcher
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from common import CONCURRENCY, URLS, finish

schema = {"name": "books", "baseSelector": "article.product_pod",
          "fields": [{"name": "title", "selector": "h3 a", "type": "attribute", "attribute": "title"},
                     {"name": "price", "selector": "p.price_color", "type": "text"}]}


async def main():
    run = CrawlerRunConfig(extraction_strategy=JsonCssExtractionStrategy(schema), cache_mode=CacheMode.BYPASS,
                           verbose=False)
    items, errors = [], 0
    async with AsyncWebCrawler(config=BrowserConfig(headless=True, verbose=False)) as crawler:
        results = await crawler.arun_many(URLS, config=run, dispatcher=SemaphoreDispatcher(semaphore_count=CONCURRENCY))
        for r in results:
            if r.success and r.extracted_content:
                items += json.loads(r.extracted_content)
            else:
                errors += 1
    finish(items, errors)

asyncio.run(main())
