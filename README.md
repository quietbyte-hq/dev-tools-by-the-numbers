# dev-tools-by-the-numbers

Weekly adoption numbers for AI and developer tools, collected by Quietbyte (AI & dev tools by the numbers). Every number in our videos comes from these files.

## PyPI downloads, week ending 2026-10-11

| Tool | Package | Downloads | vs previous week |
|---|---|--:|--:|
| Requests | `requests` | 310,635,492 | +3% |
| HTTPX | `httpx` | 160,875,391 | +3% |
| pandas | `pandas` | 143,582,496 | +3% |
| pip | `pip` | 101,840,026 | +3% |
| Ruff | `ruff` | 83,544,305 | +4% |
| OpenAI SDK | `openai` | 76,138,589 | +3% |
| Beautiful Soup | `beautifulsoup4` | 68,614,729 | -1% |
| MCP Python SDK | `mcp` | 61,275,340 | +2% |
| Hugging Face Hub | `huggingface-hub` | 59,498,455 | +0% |
| Anthropic SDK | `anthropic` | 41,718,558 | +4% |
| LangChain | `langchain` | 36,001,937 | -11% |
| uv | `uv` | 31,636,183 | -1% |
| Black | `black` | 28,394,734 | +3% |
| Playwright | `playwright` | 26,049,365 | +3% |
| Transformers | `transformers` | 24,289,038 | -4% |

## Findings from our scrapers

Measured with our own Apify Actors on fixed samples, re-run monthly. Counts only; the job ads themselves belong to the employers and job boards and are not included.

| Month | Finding | Tool |
|---|---|---|
| 2026-10 | 79% of job ads at big H-1B sponsors never mention visas | [workday-jobs-visa](https://apify.com/quietbyte/workday-jobs-visa) |
| 2026-10 | 59% of these 'remote' jobs are open to US residents only | [remote-jobs-by-country](https://apify.com/quietbyte/remote-jobs-by-country) |
| 2026-10 | 29 of 30 UK job ads that mention visa sponsorship refuse it | [reed-jobs-uk-visa](https://apify.com/quietbyte/reed-jobs-uk-visa) |
| 2026-10 | Only 10 of 98 top podcasts publish a transcript in their feed | [podcast-transcripts](https://apify.com/quietbyte/podcast-transcripts) |

## Videos

- 2026-10-18 · Video: [AI & dev tools by the numbers: 2026-W42](https://youtu.be/Eyn3ca1tsPI)
- 2026-10-17 · Short: [79% of job ads at big H-1B sponsors never mention visas](https://youtube.com/shorts/prOnzR997Mk)
- 2026-10-16 · Short: [LangChain vs Pydantic AI vs LlamaIndex vs CrewAI: real PyPI download data (Oct 2026)](https://youtube.com/shorts/vhWIHusCwo8)
- 2026-10-15 · Short: [Crawlee downloads +26% in a week](https://youtube.com/shorts/Ttw_WLyqzrw)
- 2026-10-15 · Video: [LangChain vs Pydantic AI vs LlamaIndex vs CrewAI: real PyPI download data (Oct 2026)](https://youtu.be/gVIjyLgEE_w)
- 2026-10-14 · Short: [#1 trending on Hugging Face: google/embeddinggemma-2](https://youtube.com/shorts/HDwa4fuYvA4)

## Files

| File | What | Source |
|---|---|---|
| `data/pypi-weekly.csv` | Downloads per package per week (Mon-Sun) | [pypistats.org](https://pypistats.org), without mirrors |
| `data/npm-weekly.csv` | Downloads per package per week (Mon-Sun) | [npm downloads API](https://github.com/npm/registry/blob/main/docs/download-counts.md) |
| `data/github.csv` | Stars, forks and open issues, one row per repo per day | [GitHub REST API](https://docs.github.com/rest) |
| `data/huggingface-trending.csv` | Trending models with likes and 30-day downloads | [Hugging Face Hub API](https://huggingface.co/docs/hub/api) |
| `data/actor-findings.json` | Findings from our Apify Actors: the counts behind each number, with the sample described in `source` | our Actors at [apify.com/quietbyte](https://apify.com/quietbyte) |
| `bench/scrapers/` + `data/bench-scrapers-*.json` | Our hands-on scraper test: same 50 pages for every tool, 3 runs, fresh container, 2 GB cap | run it yourself: `python crawl_scrapy.py` etc. |

## Notes

- Downloads include CI servers and mirrors, so they measure popularity, not people.
- Registries sometimes change how they count. When most big packages jump or drop on the same day, weeks before that day are left out, so no table compares across the change.
- Updated automatically. Numbers are as the sources reported them on the day collected.

## License

The compiled tables are CC BY 4.0: credit "Quietbyte, dev-tools-by-the-numbers". The underlying numbers belong to their sources above.
