from nimbuscasino.coinflip import coinflip
import random

print("🎰 Welcome to NimbusCasino: Coin Flip Edition 🎰")
rng = random.Random()

credits = 100
while True:
    print(f"\n💰 Current credits: {credits}")
    guess = input("Guess 'heads' or 'tails' (or type 'quit' to exit): ").strip().lower()
    if guess == "quit":
        print(f"👋 Thanks for playing! Final credits: {credits}")
        break
    if guess not in ["heads", "tails"]:
        print("❌ Invalid input, please type 'heads' or 'tails'.")
        continue

    try:
        bet = int(input("Enter your bet amount: "))
    except ValueError:
        print("❌ Invalid bet! Please enter a number.")
        continue

    res = coinflip(guess, bet=bet, rng=rng)
    if res["win"]:
        print(f"✅ It was {res['flip']}! You WIN 🥳 +{res['payout']} credits")
    else:
        print(f"💀 It was {res['flip']}! You LOSE 😭 {res['payout']} credits")

    credits += res["payout"]
