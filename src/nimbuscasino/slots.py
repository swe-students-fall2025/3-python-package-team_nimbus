# slots.py

# first line for future type hints
from __future__ import annotations

# import libraries
import random
from typing import Optional, TypedDict, Dict, List, Literal

# info for one winning line
class SlotsLineInfo(TypedDict):
    symbol: str
    count: int
    payout: int

# full result of one spin
class SlotsResult(TypedDict):
    game: Literal["slots"]
    grid: List[List[str]]
    lines: Dict[str, SlotsLineInfo]
    total_payout: int

# symbols, odds, and payout table
DEFAULT_SYMBOLS = ["🍒", "🍋", "🔔", "⭐", "7"]
DEFAULT_WEIGHTS = [30, 25, 20, 15, 10]
DEFAULT_PAYTABLE = {
    "🍒": {3: 5},
    "🍋": {3: 6},
    "🔔": {3: 12},
    "⭐": {3: 20},
    "7": {2: 5, 3: 50},
}

# 5 standard winning lines
LINES = {
    "top": [(0, 0), (0, 1), (0, 2)],
    "middle": [(1, 0), (1, 1), (1, 2)],
    "bottom": [(2, 0), (2, 1), (2, 2)],
    "diag_down": [(0, 0), (1, 1), (2, 2)],
    "diag_up": [(2, 0), (1, 1), (0, 2)],
}

# do one spin and return result
def spin_slots(
    bet: int = 1,
    rng: Optional[random.Random] = None,
    symbols: Optional[List[str]] = None,
    weights: Optional[List[int]] = None,
    paytable: Optional[Dict[str, Dict[int, int]]] = None,
    rows: int = 3,
    cols: int = 3,
) -> SlotsResult:
    # check inputs
    if not isinstance(bet, int) or bet <= 0:
        raise ValueError("bet must be positive")
    if rows <= 0 or cols <= 0:
        raise ValueError("rows and cols must be positive")

    # choose random and settings
    r = rng or random.Random()
    syms = symbols or DEFAULT_SYMBOLS
    wts = weights or DEFAULT_WEIGHTS
    pt = paytable or DEFAULT_PAYTABLE

    # make grid (3x3)
    grid: List[List[str]] = [[None] * cols for _ in range(rows)]  # type: ignore
    for c in range(cols):
        for rr in range(rows):
            grid[rr][c] = r.choices(syms, wts, k=1)[0]

    # check lines for wins
    lines_out: Dict[str, SlotsLineInfo] = {}
    total = 0
    for name, coords in LINES.items():
        if any(rr >= rows or cc >= cols for rr, cc in coords):
            continue
        seq = [grid[rr][cc] for rr, cc in coords]
        if seq[0] == seq[1] == seq[2]:
            sym = seq[0]
            mult = pt.get(sym, {}).get(3, 0)
            payout = bet * mult
            if payout:
                lines_out[name] = SlotsLineInfo(symbol=sym, count=3, payout=payout)
                total += payout
        elif seq.count("7") == 2:
            mult = pt.get("7", {}).get(2, 0)
            payout = bet * mult
            if payout:
                lines_out[name] = SlotsLineInfo(symbol="7", count=2, payout=payout)
                total += payout

    # return everything
    return SlotsResult(game="slots", grid=grid, lines=lines_out, total_payout=total)

# game loop (run this file to play)
if __name__ == "__main__":
    rng = random.Random()
    print("🎰 Welcome to NimbusCasino: Slots Edition 🎰")
    credits = 100

    while True:
        print(f"\n💰 Current credits: {credits}")
        cmd = input("Type 'spin' to play, 'quit' to exit: ").strip().lower()

        if cmd == "quit":
            print(f"👋 Thanks for playing! Final credits: {credits}")
            break
        if cmd != "spin":
            print("❌ Type 'spin' or 'quit'.")
            continue

        try:
            bet = int(input("Enter your bet amount: "))
        except ValueError:
            print("❌ Bet must be a number.")
            continue
        if bet <= 0:
            print("❌ Bet must be positive.")
            continue
        if bet > credits:
            print("❌ Not enough credits.")
            continue

        res = spin_slots(bet=bet, rng=rng)
        print("🧩 Grid:")
        for row in res["grid"]:
            print("  ", " | ".join(row))

        if res["lines"]:
            print("🏆 Line wins:")
            for line, info in res["lines"].items():
                print(f"  {line}: {info['count']}×{info['symbol']} → +{info['payout']}")
        else:
            print("— No wins —")

        payout = res["total_payout"]
        net = payout - bet
        credits = credits - bet + payout

        if net >= 0:
            print(f"✅ WIN +{net} (payout {payout} on bet {bet})")
        else:
            print(f"💀 LOSS {net} (payout {payout} on bet {bet})")
            