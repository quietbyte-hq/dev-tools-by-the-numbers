"""Shared by every crawl script: the fixed job, the result format and the container's peak memory."""
import json
import re
import sys
import time

URLS = [f"https://books.toscrape.com/catalogue/page-{n}.html" for n in range(1, 51)]   # 50 pages x 20 books
CONCURRENCY = 8
START = time.perf_counter()


def peak_mb():
    try:
        return round(int(open("/sys/fs/cgroup/memory.peak").read()) / 1e6, 1)
    except OSError:
        return None


def finish(items, errors=0):
    """Print one JSON line: what was extracted, how long it took, peak memory of the whole container."""
    titles = {i["title"] for i in items if i.get("title")}
    prices = [float(re.sub(r"[^\d.]", "", i["price"])) for i in items if i.get("price") and re.search(r"\d", i["price"])]
    print(json.dumps({"items": len(items), "unique_titles": len(titles), "prices_parsed": len(prices),
                      "seconds": round(time.perf_counter() - START, 2), "peak_mb": peak_mb(), "errors": errors}))
    sys.stdout.flush()
