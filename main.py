import random
import time
import math
import os

Balance = 200
GamesPlayed = 0
GamesWon = 0
GamesLost = 0



while True:
			
		
		
	print("Balance: ", Balance)
	wager = type=int(input("Wager: "))
	if wager > Balance:
		print("Wager higher than balance. Set to", Balance)
		wager = Balance
		time.sleep(1)
		os.system("clear")
	else:
		pass
	os.system("clear")
	bet = type=int(input("Prediction: "))
	if bet > 6:
		print("Dice only rolls up to 6")
	else:
		pass
		if bet < 0:
			print("Dice only rolls from 1 to 6")
		else:
			pass
	os.system("clear")
	print(f"You're betting ${wager} on the dice rolling on {bet}")
	confirm = input("Confirm? (Y/N)")
	confirm.lower()
	if confirm == "y" or "yes":
		os.system("clear")
		pass
	else:
		print("will do later")
	
	s = [1,2,3,4,5,6]
	
	selection = random.randrange(len(s))
	print("Rolled: ", s[selection])
	if s[selection] == bet:
		Balance = Balance + wager
		Balance * 6
		nb = round(Balance)
		Balance = nb
		print("New Balance: ", Balance)
		time.sleep(3)
		os.system("clear")
	else:
		Balance = Balance - wager
		Balance / 6
		nb = round(Balance)
		Balance = nb
		print("New Balance: ", Balance)
		time.sleep(3)
		os.system("clear")
