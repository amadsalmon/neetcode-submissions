# NeetCode Submissions

Everything in this repository is automatic.

- Solutions are pushed here by [NeetCode](https://neetcode.io)'s GitHub Sync every time I submit on the platform - nothing is hand-picked or cleaned up after the fact.
- This README, including the stats and the highlighted solutions below, is generated and kept up to date automatically by my AI assistant. It refreshes as new submissions land, so what you're reading always reflects the current state of the repo.

What you see is the actual working process, not a curated portfolio.

## At a glance

- **110+ problems** synced across data structures & algorithms, SQL, and design patterns
- **200+ commits** since June 2026 - one per submission, retries included
- **50+ problems** carry multiple submissions, so the path from first attempt to final version stays visible in the file history
- **Python 3** throughout, plus SQL

## How it's organized

```
Data Structures & Algorithms/<problem>/submission-N.py
SQL/<problem>/submission-N.sql
Design Patterns/<pattern>/submission-N.py
```

`submission-0` is the first attempt; later attempts on the same problem get their own numbered files, in order.

## What the submissions show

- **Reasoning written down, not just code.** In [median-of-two-sorted-arrays](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/median-of-two-sorted-arrays/submission-0.py), the docstring works from brute force to an O(n) merge and then to the O(log n) partition insight before the binary search implementation.
- **Iteration kept in the file.** [products-of-array-discluding-self](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/submission-4.py) keeps the naive O(n^2) version in the same file as the O(n) prefix/suffix pass, both labeled.
- **The classic hards, done properly.** [trapping-rain-water](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/trapping-rain-water/submission-0.py) with precomputed maxes, [sliding-window-maximum](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/sliding-window-maximum/submission-0.py) with a real monotonic deque, and a [hand-rolled LRU cache](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/lru-cache/submission-4.py) built on an explicit doubly linked list.
- **Persistence on the ones that fight back.** [minimum-window-with-characters](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/minimum-window-with-characters/submission-15.py) is the fifteenth submission on that problem - and the one that lands the clean two-pointer with early exit.

## Auto-selected highlights

Chosen by the automated review, which re-reads the repo and refreshes this list as stronger solutions land.

| Problem | What it demonstrates |
| --- | --- |
| [median-of-two-sorted-arrays](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/median-of-two-sorted-arrays/submission-0.py) | Hard. Full written derivation from brute force to O(log n), clean edge handling |
| [trapping-rain-water](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/trapping-rain-water/submission-0.py) | Hard. O(n) time with precomputed left/right maxes |
| [sliding-window-maximum](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/sliding-window-maximum/submission-0.py) | Hard. Monotonic deque, textbook shape |
| [minimum-window-with-characters](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/minimum-window-with-characters/submission-15.py) | Hard. Fifteen attempts kept; the final one is a clean two-pointer with early exit |
| [lru-cache](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/lru-cache/submission-4.py) | Hand-rolled doubly linked list plus hash map |
| [products-of-array-discluding-self](https://github.com/amadsalmon/neetcode-submissions/blob/main/Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/submission-4.py) | Brute force and optimal kept side by side in one file |

---

<sub>Synced automatically from [NeetCode.io](https://neetcode.io) via GitHub Sync. This README is generated and maintained automatically; last refresh November 2026.</sub>
