import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction.")

bids = {}

def finds_highest_bidder(bidding_record):
 highest_bid = 0
 winner = ""
 for bidder in bidding_record:
  if bidding_record[bidder] > highest_bid:
   highest_bid = bidding_record[bidder] 
   winner = bidder

 print(f"The winner is {winner} with a bid of ${highest_bid}")

next_bidder = True
while next_bidder:
 name = input("What's your name? ")
 amount = float(input("What's your bid? $"))

 bids[name] = amount
 
 another_bidder = input("Are there any other bidders? 'yes' or 'no' ").lower()
 if another_bidder == "yes":
  next_bidder
  os.system('cls||clear')
 elif another_bidder == "no":
  next_bidder = False
  os.system('cls||clear')
  finds_highest_bidder(bidding_record = bids)
  

