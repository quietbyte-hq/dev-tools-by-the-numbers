# dev-tools-by-the-numbers

Weekly adoption numbers for AI and developer tools, collected by Quietbyte (AI & dev tools by the numbers). Every number in our videos comes from these files.

## PyPI downloads, week ending 2026-10-25

| Tool | Package | Downloads | vs previous week |
|---|---|--:|--:|
| Requests | `requests` | 328,188,328 | +4% |
| HTTPX | `httpx` | 178,471,438 | +6% |
| pandas | `pandas` | 149,934,696 | +3% |
| pip | `pip` | 135,806,037 | +31% |
| Ruff | `ruff` | 94,109,539 | +7% |
| OpenAI SDK | `openai` | 83,852,628 | +3% |
| Beautiful Soup | `beautifulsoup4` | 72,539,415 | +4% |
| MCP Python SDK | `mcp` | 70,182,218 | +8% |
| Hugging Face Hub | `huggingface-hub` | 63,049,972 | +1% |
| Anthropic SDK | `anthropic` | 44,777,051 | +6% |
| uv | `uv` | 37,642,696 | +9% |
| LangChain | `langchain` | 37,534,014 | +1% |
| Playwright | `playwright` | 29,446,601 | +5% |
| Black | `black` | 28,052,209 | +2% |
| Transformers | `transformers` | 25,738,854 | +4% |

## Findings from our scrapers

Measured with our own Apify Actors on fixed samples, re-run monthly. Counts only; the job ads themselves belong to the employers and job boards and are not included.

| Month | Finding | Tool |
|---|---|---|
| 2026-10 | 79% of job ads at big H-1B sponsors never mention visas | [workday-jobs-visa](https://apify.com/quietbyte/workday-jobs-visa) |
| 2026-10 | 59% of these 'remote' jobs are open to US residents only | [remote-jobs-by-country](https://apify.com/quietbyte/remote-jobs-by-country) |
| 2026-10 | 29 of 30 UK job ads that mention visa sponsorship refuse it | [reed-jobs-uk-visa](https://apify.com/quietbyte/reed-jobs-uk-visa) |
| 2026-10 | Only 10 of 98 top podcasts publish a transcript in their feed | [podcast-transcripts](https://apify.com/quietbyte/podcast-transcripts) |

## Videos

- 2026-10-27 · Short: [Scrapy downloads +27% in a week](https://youtube.com/shorts/3ZnEvSi6o7Y)
- 2026-10-26 · Short: [#4 trending on Hugging Face: black-forest-labs/flux-3-image-klein](https://youtube.com/shorts/cXkUS2aIALY)
- 2026-10-25 · Short: [LiquidAI: LFM2.5-24B-A2B: $0.05 per million input tokens](https://youtube.com/shorts/aa9tbhozlHM)
- 2026-10-25 · Video: [AI & dev tools by the numbers: 2026-W43](https://youtu.be/nW6dSG7QUQE)
- 2026-10-24 · Short: [59% of these 'remote' jobs are open to US residents only](https://youtube.com/shorts/SBygL37pp_E)
- 2026-10-24 · Short: [#2 trending on Hugging Face: black-forest-labs/flux-3-image-klein-comfy](https://youtube.com/shorts/ztcOj_msJZ4)
- 2026-10-23 · Short: [AI agents that reverse-engineer games: 8,089 GitHub stars in 17 days](https://youtube.com/shorts/LWBFbDGK5Tc)
- 2026-10-23 · Short: [Crawlee downloads +29% in a week](https://youtube.com/shorts/fVOv7zbbDmU)
- 2026-10-22 · Short: [Google: Nano Banana 2.1: $1.5 per million input tokens](https://youtube.com/shorts/ZfZyGJwfmJQ)
- 2026-10-22 · Video: [Who's gaining ground: Playwright vs Selenium (Oct 2026)](https://youtu.be/YbhEN-qBgo0)
- 2026-10-21 · Short: [pip vs uv vs Poetry vs PDM: real PyPI download data (Oct 2026)](https://youtube.com/shorts/GpBevHVdJiE)
- 2026-10-21 · Short: [#1 trending on Hugging Face: deepseek-ai/DeepSeek-V4.1-Flash-1017](https://youtube.com/shorts/N1p9AcaNlV4)
- 2026-10-21 · Short: [Anthropic: Claude Haiku 5.5: $0.1 per million input tokens](https://youtube.com/shorts/Hvgo7wZMc80)
- 2026-10-20 · Short: [jev-ultrafast: 22,965 GitHub stars in 29 days](https://youtube.com/shorts/77ZjSUZdGK0)
- 2026-10-20 · Video: [Is pip still the default? PyPI numbers vs uv, Poetry, PDM](https://youtu.be/rw4fZZTtPMc)
- 2026-10-20 · Short: [Free rebuilds of 7 Adobe apps: 128,309 GitHub stars in 17 days](https://youtube.com/shorts/aDBxRyiYAm0)
- 2026-10-19 · Short: [open_scion: 1,029 GitHub stars in 1 day](https://youtube.com/shorts/KS7i2OmPJU0)
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
