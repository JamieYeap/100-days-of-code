from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid amount of ${highest_bid}.")


bidding_price = {}
continue_bid = True
while continue_bid:
    bidder_name = input("What is your name?\n")
    bid = float(input("What's your bid?\n$"))
    bidding_price[bidder_name] = bid

    print("Anyone else want to bid?")
    bid_yes_no = input("Type 'yes' to continue. Type 'no' to stop bidding.\n")
    if bid_yes_no == 'no':
        continue_bid = False
        print("The bidding has ended")
        find_highest_bid(bidding_price)
    elif bid_yes_no == 'yes':
        clear()


