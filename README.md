# 🎰 NimbusCasino
![Python build & test](https://github.com/swe-students-fall2025/3-python-package-team_nimbus/actions/workflows/event-logger.yml/badge.svg)



**nimbuscasino** is a lightweight and testable Python package with four classic chance-based mini-games:

- Rock-Paper-Scissors
- Coin Flip
- Roulette (Red/Black)
- Slots (3×3)

All game functions are **pure** (no input/print, no global state) and return structured results, so you can plug them into chatbots, simulations, or your own program.


⚠️ *This package is for entertainment and educational use only — no real gambling or monetary transactions are involved.*


## Team Members
| Name | GitHub Profile |
|------|----------------|
| Asim | [@asimd0](https://github.com/asimd0) |
| Matt | [@m9membreno](https://github.com/m9membreno) |
| Tup  | [@treejitsu](https://github.com/treejitsu) |
| Elia | [@YilinWu1028](https://github.com/YilinWu1028) |
| Mojin| [@Mojin-Yuan](https://github.com/Mojin-Yuan) |



## Installation
#### PyPi page
https://pypi.org/project/nimbuscasino/


#### 1) Install pipenv (if needed)
```bash
pip install pipenv
```
#### 2) Create/activate a virtual environment
```bash
pipenv shell
```
#### 3) Install nimbuscasino from PyPi
```bash
pipenv install nimbuscasino
```
#### Verify your installation in python:
```python
from nimbuscasino.rps import rps
print(rps("rock"))
```

## Usage:
Each game function returns a dictionary containing details of the outcome.  
You control any printing, UI, or balance-handling.  
**Note:** Each function accepts an optional pseudo-random generator (`rng`) to support deterministic testing. You can ignore this in normal gameplay.

---

#### 1) Rock-Paper-Scissors — `rps(player, bet=1, rng=None)`

**Arguments**
| Name | Type | Description |
|------|------|-------------|
| `player` | `"rock"`, `"paper"`, or `"scissors"` | Your selection |
| `bet` | number > 0 | Wager amount |
| `rng` | optional | Must support `.choice(seq)` if provided |

**Return Example**
```python
{
  "game": "rps",
  "player": "rock",
  "computer": "scissors",
  "result": "win" | "lose" | "tie",
  "payout": 5
}
```

**Example Usage**
```python
from nimbuscasino.rps import rps
res = rps("rock", bet=5)
print(res)
```

---

#### 2) Coin Flip — `coinflip(guess, bet=1, rng=None, bias=0.5)`

**Arguments**
| Name | Type | Description |
|------|------|-------------|
| `guess` | `"heads"` or `"tails"` | Your call |
| `bet` | positive integer | Wager |
| `rng` | optional | Must support `.random()` → float in [0,1) |
| `bias` | float (0.0–1.0) | Probability of heads |

**Return Example**
```python
{
  "game": "coinflip",
  "guess": "heads",
  "flip": "heads" | "tails",
  "win": True | False,
  "payout": 1 | -1 | ...,
  "prob_heads": 0.5
}
```

**Example Usage**
```python
from nimbuscasino.coinflip import coinflip
res = coinflip("heads", bet=2)
print(res)
```

---

#### 3) Roulette (Red/Black) — `roulette_color(color, bet=1, rng=None)`

**Arguments**
| Name | Type | Description |
|------|------|-------------|
| `color` | `"red"` or `"black"` | Color to bet on |
| `bet` | number > 0 | Wager |
| `rng` | optional | Must support `.choice(seq)` |

**Return Example**
```python
{
  "result": True | False,
  "spin": "red" | "black" | "green",
  "payout": 10 | -10 | ...
}
```

**Example Usage**
```python
from nimbuscasino.roulette import roulette_color
res = roulette_color("red", bet=10)
print(res)
```

---

#### 4) Slots — `spin_slots(bet=1, rng=None, symbols=None, weights=None, paytable=None, rows=3, cols=3)`

**Arguments**
| Name | Description |
|------|-------------|
| `bet` | Amount wagered per spin |
| `rng` | Optional random source supporting `.choices()` |
| `symbols`, `weights`, `paytable` | Optional custom reel configuration |
| `rows`, `cols` | Dimensions of slot grid (Default: 3×3) |

**Return Example**
```python
{
  "game": "slots",
  "grid": [["🍋","🔔","🍋"], ["🍋","⭐","🍋"], ["🍒","🔔","🍋"]],
  "lines": { "middle": {"symbol":"🍋","count":3,"payout":6}, ... },
  "total_payout": 6
}
```

**Example Usage**
```python
from nimbuscasino.slots import spin_slots
res = spin_slots(bet=3)
print(res)
```

---

### Interactive Example Program

A demo is included for trying all four games:

**File:** `example.py`  
https://github.com/swe-students-fall2025/3-python-package-team_nimbus/blob/pipfile-experiment/example.py

Run it:
```bash
python example.py
```

---

### Contributing (Local Development Setup)

```bash
# Clone repository
git clone https://github.com/swe-students-fall2025/3-python-package-team_nimbus.git
cd 3-python-package-team_nimbus

# Create / activate virtual environment
pipenv shell

# Install development dependencies
pipenv install --dev

# Install package in editable mode
pip install -e .

# Run test suite
pytest

# Build distributable packages
python -m build
```

#### (Optional) Upload Build to TestPyPI
```bash
twine upload --repository testpypi dist/*
```






