
import random
from nimbuscasino.roulette import roulette_color
from nimbuscasino.rps import rps
from nimbuscasino.coinflip import coinflip
from nimbuscasino.slots import spin_slots

def prompt_bet(credits: int) -> int:
    while True:
        try:
            bet = int(input("Enter your bet amount: ").strip())
        except ValueError:
            print("❌ Bet must be a number.")
            continue
        if bet <= 0:
            print("❌ Bet must be positive.")
        elif bet > credits:
            print("❌ Not enough credits.")
        else:
            return bet


def play_roulette_mode(credits: int) -> int:
    print("\n🎡 Roulette — bet on red/black")
    color = input("Pick 'red' or 'black': ").strip().lower()
    if color not in {"red", "black"}:
        print("❌ Invalid color.")
        return credits
    bet = prompt_bet(credits)

    res = roulette_color(color, bet=bet)
    print(f"Spin: {res['spin']}")
    net = res["payout"]
    credits += net
    print(f"{'✅ WIN' if res['result'] else '💀 LOSS'} {net:+} (payout {res['payout']} on bet {bet})")
    return credits


def play_rps_mode(credits: int) -> int:
    print("\n✊🖐️✌️ Rock-Paper-Scissors")
    move = input("Choose 'rock', 'paper', or 'scissors': ").strip().lower()
    if move not in {"rock", "paper", "scissors"}:
        print("❌ Invalid choice.")
        return credits
    bet = prompt_bet(credits)

    res = rps(move, bet=bet)
    print(f"Computer: {res['computer']} → Result: {res['result'].upper()}")
    net = res["payout"]
    credits += net
    print(f"{'✅ WIN' if net > 0 else ('➖ TIE' if net == 0 else '💀 LOSS')} {net:+}")
    return credits


def play_coinflip_mode(credits: int) -> int:
    print("\n🪙 Coinflip")
    guess = input("Guess 'heads' or 'tails': ").strip().lower()
    if guess not in {"heads", "tails"}:
        print("❌ Invalid guess.")
        return credits
    bet = prompt_bet(credits)

    res = coinflip(guess, bet=bet)
    print(f"Flip: {res['flip']} → {'WIN' if res['win'] else 'LOSS'}")
    net = res["payout"]
    credits += net
    print(f"{'✅ WIN' if net > 0 else '💀 LOSS'} {net:+}")
    return credits


def play_slots_mode(credits: int) -> int:
    # Uses the same interactive flow you had in slots; only wrapped to share credits.
    print("\n🎰 Slots")
    bet = prompt_bet(credits)
    res = spin_slots(bet=bet)

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
    credits += net
    if net >= 0:
        print(f"✅ WIN {net:+} (payout {payout} on bet {bet})")
    else:
        print(f"💀 LOSS {net} (payout {payout} on bet {bet})")
    return credits


def main():
    credits = 100
    MENU = {
        "1": ("Roulette", play_roulette_mode),
        "2": ("Rock-Paper-Scissors", play_rps_mode),
        "3": ("Coinflip", play_coinflip_mode),
        "4": ("Slots", play_slots_mode),
        "q": ("Quit", None),
    }

    print("🎮 NimbusCasino Example")
    while True:
        print(f"\n💰 Credits: {credits}")
        if credits <= 0:
            print("👋 Thanks for playing! (no credits)")
            break
        for k, (label, _) in MENU.items():
            print(f"  {k}) {label}")
        choice = input("Select: ").strip().lower()

        if choice == "q":
            print(f"👋 Thanks for playing! Final credits: {credits}")
            break
        if choice not in MENU or MENU[choice][1] is None:
            print("❌ Invalid selection.")
            continue

        _, handler = MENU[choice]
        credits = handler(credits)


if __name__ == "__main__":
    main()