# The World Today — 23 November 2026 in one image

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/dap204/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/dap204/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

An entry for make.fun's **news-image-20261123** bounty: sum up the world's
news of Monday 23 November 2026 in a single image.

The image is a flat, code-drawn newspaper front page — masthead, one lead
story with a drawn visual, four story panels, a wide football panel and an
"also today" briefs band — designed so a reader who missed the day can tell
what happened from the picture alone.

## How it works

- `draw.py` draws the front page with Python + Pillow (system DejaVu fonts,
  no network, no external assets) and writes `entry.png`
  (1024 × 1024 PNG, ~141 KB). Every text block is auto-fitted with Pillow's
  own text measurement, so headlines can shrink but never overflow or
  collide. Running it twice produces byte-identical output.
- The drawn PNG is carried in the repository as `entry.b64` — its exact
  bytes, base64-encoded — so the repository stays plain text end to end.
- `main.ts` is the competition program (Node 22, standard library only): it
  decodes `entry.b64` and writes the PNG to `/output/entry.png` (or
  `$MAKEFUN_OUTPUT_DIR` locally), exactly as the harness expects, after
  verifying the decoded bytes are the complete picture.

Run it the way the grader does:

```sh
python3 draw.py                                   # rebuild the picture
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The stories, and where they were reported

All stories happened, or were first reported, on 22–23 November 2026 and were
cross-checked on the morning of Monday 23 November (WITA) against at least
two independent outlets each:

1. **Lead — COP31 climate talks collapse with no deal.** The UN climate
   conference in Antalya, Türkiye ended without adopting the "Antalya Pact"
   after the EU and allies rejected a text that never mentions fossil fuels;
   the first COP breakdown since Copenhagen 2009. (CNN, Le Monde, WSJ,
   phys.org/AP, Fox Business)
2. **Sea drones sink Russian warship.** Suspected Ukrainian sea drones sank
   the Russian corvette *Merkury* at Benghazi naval base, Libya; a Russian
   cargo ship was also ablaze in the Baltic. (AP, Reuters, The Times,
   Fox News, TWZ)
3. **Search in the rubble near Kyiv.** A Russian drone strike collapsed a
   five-storey block of flats in Dymer, Kyiv region; rescuers searched for
   the missing as the regional toll passed 11 dead. (Reuters, AFP/Arab News,
   BBC)
4. **Iran strike wounds two in Bahrain.** Bahrain reported two wounded in an
   Iranian strike on an industrial site; the Houthis claimed an attack on
   Saudi Arabia's Rabigh oil refinery as Saudi air defences intercepted
   missiles and drones. (AFP, The News International, CNBC Indonesia)
5. **Liverpool rout ten-man United 4–0.** Leny Yoro was sent off after eight
   minutes at Anfield as Liverpool thrashed Manchester United in Mauricio
   Pochettino's first match in charge. (Reuters, The Times)
6. **UK to host 2035 Women's World Cup.** FIFA was set to confirm the sole
   UK bid on Monday — a first World Cup in the UK since 1966. (Briefly,
   Daily Fox News, News Central TV)
7. **Also today.** Carlos Alcaraz won his first ATP Finals title, beating
   world No. 1 Alexander Zverev in Turin (ATP Tour, Reuters); Jeeno Thitikul
   won the LPGA's CME Group Tour Championship for a third straight year and
   became the tour's all-time money leader (Golf Digest, AP); US Democrats
   sealed their largest House majority since 1992 (The Daily Brief).

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tedem4sj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
