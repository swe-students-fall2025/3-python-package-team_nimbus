# 🎰 NimbusCasino
![Python build & test](https://github.com/swe-students-fall2025/3-python-package-team_nimbus/actions/workflows/ci.yml/badge.svg)


**nimbuscasino** is a lightweight and testable Python package with four classic chance-based mini-games:

- Rock-Paper-Scissors
- Coin Flip
- Roulette (Red/Black)
- Slots (3×3)

All game functions are **pure** (no input/print, no global state) and return structured results, so you can plug them into chatbots, simulations, or your own program.


⚠️ *This package is for entertainment and educational use only — no real gambling or monetary transactions are involved.*


## 👥 Team Members
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


### Example Programs
- [example.py](https://github.com/swe-students-fall2025/3-python-package-team_nimbus/blob/pipfile-experiment/example.py)






