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
  (1024 × 1024 PNG, ~147 KB). Every text block is auto-fitted with Pillow's
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
two independent outlets each, then re-checked with final figures on the
evening of Tuesday 24 November (WITA) — this is the v2 refresh, which corrects
the Dymer toll, the Gulf panel and the FIFA confirmation, and swaps the
weakest panel (Liverpool 4–0 United) for the day's biggest market story,
Nvidia's CEO comeback:

1. **Lead — COP31 climate talks collapse with no deal.** The UN climate
   conference in Antalya, Türkiye ended without adopting the "Antalya Pact"
   after the EU and allies rejected a text that never mentions fossil fuels;
   the longest COP ever, and the first COP breakdown since Copenhagen 2009.
   (CNN, Le Monde, WSJ, phys.org/AP, Fox Business)
2. **Sea drones sink Russian warship.** Seven Ukrainian sea drones sank the
   Russian corvette *Merkury* at Benghazi naval base, Libya, destroying a
   Ka-27 helicopter on board; the cargo ship *Angara* was hit as well.
   (CNN, AP, Reuters, The Times, Fox News, TWZ)
3. **Search in the rubble near Kyiv.** A Russian drone strike collapsed a
   five-storey block of flats in Dymer, Kyiv region; the rescue operation
   ended on Monday evening with 11 dead, while a boy of seven and a woman
   of 79 were pulled alive from the rubble. (Reuters, AFP/Arab News, BBC,
   Kyiv Post)
4. **Houthis claim hit on Saudi refinery.** The Houthis said they struck
   the Petro Rabigh oil refinery on Saudi Arabia's Red Sea coast and claimed
   a direct hit; Riyadh stayed silent, and no damage was independently
   confirmed. (Reuters, TBS News, Yemen Monitor)
5. **Huang back at Nvidia; shares soar 31%.** Nvidia's board reinstated
   Jensen Huang as CEO days after his exit; the stock jumped 31% in a day,
   adding nearly $1 trillion in market value. (CNN, Le Monde, The Times,
   USA Today)
6. **UK to host 2035 Women's World Cup.** FIFA confirmed the UK bid —
   England, Northern Ireland, Scotland and Wales — at an Extraordinary
   Congress on Monday, a first World Cup in the UK since 1966. (FIFA,
   Reuters, BBC, The Times)
7. **Also today.** Carlos Alcaraz won his first ATP Finals title, beating
   world No. 1 Alexander Zverev in Turin (ATP Tour, Reuters); Jeeno Thitikul
   won the LPGA's CME Group Tour Championship for a third straight year and
   became the tour's all-time money leader (Golf Digest, AP); US Democrats
   sealed their largest House majority since 1992 (The Daily Brief).

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tedem4sj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
