from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
all_bidder = []
def bidder():
	new_bidder = {}
	new_bidder["name"] = input("What is your name?: ")
	new_bidder["bid"] = int(input("What's your bid?: "))
	all_bidder.append(new_bidder)
	ask = input("Any other bidder?: Type 'Yes' or 'No'\n")
	if ask.lower() == "yes":
		clear()
		bidder()
	else:
		highest_bid = 0
		for n in range(0, len(all_bidder)):
			if all_bidder[n]["bid"] > highest_bid:
				highest_bid = all_bidder[n]["bid"]
				highest_bidder = all_bidder[n]["name"]
		print(f"The winner is {highest_bidder} and the bidding ammount is {highest_bid}")

bidder()