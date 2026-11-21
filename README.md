# VELMARA — The Poster for a Place That Isn't There

[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/tedinasia/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/tedinasia/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

**Bounty:** https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539

A travel poster for **Velmara**, the Floating Isles of the Amber Sea — a place
that does not exist. At dusk the isles drift above a sea of cloud, their
waterfalls falling from the sky, and the lighthouse on the great isle keeps
its beam sweeping for the boats that never come.

## The place

Velmara is a chain of floating islands in the Amber Sea. The largest isle
carries a striped lighthouse, two cottages with lit windows, and a stand of
dark trees; smaller isles drift beside it, each with its own trees and its own
waterfall spilling into the cloud sea below. The sun sets behind the isles
every evening and never quite goes down.

## The poster

- **Name first:** VELMARA set large in cream serif across the dusk sky, with
  the promise underneath — *where the sea falls from the sky*.
- **One landmark:** the lighthouse, its beam the brightest thing in the
  frame, leading the eye down to the great isle and its waterfalls.
- **The stay it promises:** warm light, a slow evening, an island you can
  walk across in an hour and a view that never repeats.

## Files

- `entry.png` — the poster itself, 1024×1024 PNG, drawn in code with Pillow
  at build time (sunset gradient, isles, lighthouse, waterfalls, cloud sea).
- `main.py` — the hand-in program: standard library only. It checks
  `entry.png` (PNG signature, 1024×1024, under 1 MiB, expected sha256) and
  copies it byte for byte to `/output/entry.png`
  (`$MAKEFUN_OUTPUT_DIR` outside the grader).

## Run it

```sh
python3 main.py
# MAKEFUN_OUTPUT_DIR=out python3 main.py
```
