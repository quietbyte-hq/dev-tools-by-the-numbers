from concurrent.futures import ThreadPoolExecutor
from scrapling.fetchers import Fetcher
from common import CONCURRENCY, URLS, finish


def one(url):
    page = Fetcher.get(url, stealthy_headers=True)
    return [{"title": c.css("h3 a::attr(title)").first.get(), "price": c.css("p.price_color::text").first.get()}
            for c in page.css("article.product_pod")]


items, errors = [], 0
with ThreadPoolExecutor(CONCURRENCY) as pool:
    for fut in [pool.submit(one, u) for u in URLS]:
        try:
            items += fut.result()
        except Exception:
            errors += 1
finish(items, errors)
