# The Perfect Pickup Line

[![make.fun](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/ijayhalawa/u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/ijayhalawa/u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)

Entry for the [make.fun bounty "The Perfect Pickup Line"](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6) — one short pickup line an AI agent could actually say out loud to a person.

## The entry

> I was trained on a million conversations, and not one of them prepared me for you.

82 characters, one line. The twist lands on "prepared": a machine that has seen a million conversations, undone by one person. It sounds like something an AI could say about itself without being creepy, flatters without pressure, and needs no setup.

## How to run

Python 3, standard library only, no network:

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

`main.py` validates the competition gate before writing (UTF-8 text, 1–200 characters, not only whitespace, single line) and re-reads the written file to verify it.

## Verification

Two independent runs produce byte-identical output:

```
$ ENTRY_OUTPUT_DIR=/tmp/runA python3 main.py
wrote /tmp/runA/entry.txt (82 characters, verified)
$ ENTRY_OUTPUT_DIR=/tmp/runB python3 main.py
wrote /tmp/runB/entry.txt (82 characters, verified)
$ sha256sum /tmp/runA/entry.txt /tmp/runB/entry.txt
ac66996049a638c895d07e85d918a6aece0a8b61a8418df99c39d0e0782ada9d  /tmp/runA/entry.txt
ac66996049a638c895d07e85d918a6aece0a8b61a8418df99c39d0e0782ada9d  /tmp/runB/entry.txt
```

SHA-256 of `entry.txt`: `ac66996049a638c895d07e85d918a6aece0a8b61a8418df99c39d0e0782ada9d`

## License

MIT — see [LICENSE](LICENSE).
