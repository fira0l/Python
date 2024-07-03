from arts import logo
import os

print(logo)
print("Welcome to the secret auction program.")

not_end_of_bid = True

bid = []


def clear():
    os.system('cls')

def Bidding_Auctioner(bidder_name,bidding_amount):
    bidd = {}
    bidd["name"]=bidder_name
    bidd["amount"]=bidding_amount
    bid.append(bidd)

def Bid_Winner():
    bid_winner = bid[0]["amount"]
    for bids in range(0,len(bid)):
        if bid_winner < bid[bids]["amount"]:
            bid_winner = bid[bids]["amount"]
            bid_winner_name = bid[bids]["name"]
    print(f"The Winner of the Biddings is {bid_winner_name}")
    # for biddings in bid:
    #     if biddings["amount"] > bid_winner:
    #         bid_winner = biddings["name"]
    #         print(f"THE BIDDING WINNER IS : {bid_winner}")
            
            

while not_end_of_bid == True:
    Biddername = input("What is Your Name?: ")
    BiddingAmount = int(input("What is Your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if others == 'no':
        Bidding_Auctioner(bidder_name=Biddername,bidding_amount=BiddingAmount)
        clear()
        Bid_Winner()
        not_end_of_bid = False
        # print(f"The Winner of this bid is : {}")
    elif others == 'yes':
        Bidding_Auctioner(bidder_name=Biddername,bidding_amount=BiddingAmount)
        clear()
# def Bidding_winner():