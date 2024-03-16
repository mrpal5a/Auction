import os
def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found

auction_participant = {}
print("Welcome to the secret auction program")
game = True
while game:
    name = input("Enter bidders name? ")
    bid = int(input("Enter your bid?: $"))
    auction_participant[name] = bid
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if other_bidder == "yes":
        os.system('cls')                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    else:
        highest_bid = max(auction_participant.values())
        winner = get_key(auction_participant, highest_bid)
        print(f"The winner is {winner} with highest bid of ${highest_bid} ")
        print(auction_participant)
        game = False

