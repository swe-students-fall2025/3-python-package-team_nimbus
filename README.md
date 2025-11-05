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



## Installation & Virtual Environment Setup (pipenv)
### PyPi page
https://pypi.org/project/nimbuscasino/


### 1) Install pipenv (if needed)
```bash
pip install pipenv
```
### 2) Create/activate a virtual environment
```bash
pipenv shell
```
### 3) Install nimbuscasino from PyPi
```bash
pipenv install nimbuscasino
```
#### to verify your installation:
```python
from nimbuscasino.rps import rps
print(rps("rock"))
```

## How to Import and Use NimbusCasino
Developers can use the **nimbuscasino** package to easily simulate simple chance-based games inside their own Python code.
### Example Programs
- [example.py](https://github.com/swe-students-fall2025/3-python-package-team_nimbus/blob/pipfile-experiment/example.py)


## 🛠 How to Contribute
Developers who want to contribute to **NimbusCasino** can follow these steps to set up the environment, install dependencies, and run tests locally.


## 📦 Installation
NimbusCasino is available on [PyPI](https://pypi.org/project/nimbuscasino/).  
Install it with:

```bash
pip install nimbuscasino



