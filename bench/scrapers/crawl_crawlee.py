import os
os.environ.setdefault("CRAWLEE_STORAGE_DIR", "/tmp/crawlee")   # the test folder is mounted read-only
import asyncio
from crawlee import ConcurrencySettings
from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext
from common import CONCURRENCY, URLS, finish

items = []


async def main():
    crawler = BeautifulSoupCrawler(concurrency_settings=ConcurrencySettings(max_concurrency=CONCURRENCY, desired_concurrency=CONCURRENCY),
                                   max_request_retries=1)

    @crawler.router.default_handler
    async def handler(ctx: BeautifulSoupCrawlingContext) -> None:
        for card in ctx.soup.select("article.product_pod"):
            a, p = card.select_one("h3 a"), card.select_one("p.price_color")
            items.append({"title": a.get("title") if a else None, "price": p.get_text() if p else None})

    stats = await crawler.run(URLS)
    finish(items, getattr(stats, "requests_failed", 0))

asyncio.run(main())
