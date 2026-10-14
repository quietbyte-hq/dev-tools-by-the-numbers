import scrapy
from scrapy.crawler import CrawlerProcess
from common import CONCURRENCY, URLS, finish

items, errors = [], []


class Books(scrapy.Spider):
    name = "books"
    start_urls = URLS
    custom_settings = {"CONCURRENT_REQUESTS": CONCURRENCY, "LOG_LEVEL": "ERROR", "ROBOTSTXT_OBEY": True,
                       "USER_AGENT": "Mozilla/5.0 (benchmark; books.toscrape.com practice site)"}

    def parse(self, response):
        for card in response.css("article.product_pod"):
            items.append({"title": card.css("h3 a::attr(title)").get(), "price": card.css("p.price_color::text").get()})

    def errback(self, failure):
        errors.append(1)


p = CrawlerProcess()
p.crawl(Books)
p.start()
finish(items, len(errors))
