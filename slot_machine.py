import random

def spin_row():
    symbols = ['A', 'B', 'C', 'D']

    return [random.choice(symbols) for i in range(3)]

def print_row(row):
    print(" | ".join(row))
    

def get_payout(row, bet):
    if row[0] == row[1] == row[2] == row[3]:
     if row[0] == 'A':
       return bet * 3
     elif row[0] == 'B':
       return bet * 4
     elif row[0] == 'D':
        return bet *5
    return 0 
        
def main():
    balance = 100

    print("Welcome to the Slot Machine!")
    print("Symbols: [A, B, C, D]")

    while balance>0:

        print(f"\nCurrent balance: ${balance:.2f}")
        bet = input("Enter your bet amount : ")
        if not bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance for this bet.")
            continue

        if bet <= 0:
            print("Bet amount must be positive.")
            continue

        balance = balance - bet

        row = spin_row()
        print("Spinning the slot machine...")
        print_row(row)

        payout = get_payout(row, bet)
        
        if payout > 0:
           print(f"You won rs{payout}")
        else:
           print("Sorry you lost")

        balance += payout

if __name__ == "__main__":
         main()