# This program will create a persistance on the portfolio tracking system in order for the user/investor to keep his/her cash and stocks assets portfolio information
# Created by: Edgar Alan Emmanuel B. Tiamzon III
# B1L
# 10/24/23

import Tiamzon_ex7_files

# Global variable
# Dictionary
stocks = {
		"CASH": ["Cash", 10000.00, 1.00]
		}

# Build Menu
def menu():
	print(
	" ============MENU========== \n"
	" [1] View Portfolio        \n"
	" [2] Buy Stock              \n"
	" [3] Sell Stock             \n"
	" [4] Change Stock Price     \n"
	" [5] Liquidate All Stocks   \n"
	" [6] Load Portfolio         \n"
	" [7] Save Portfolio         \n"
	" [0] Exit                   \n"
	" ========================== \n", 
	end=""
	)
	
	option = int(input("Enter option: "))
	return option

# Enables to view the user's portfolio where the adding/changing of stocks happens
def viewPortfolio(stocks):
	print()
	print( "===============================PORTFOLIO===================================")
	print( "Symbol       Description        Quantity         Price            Value    ")
	print( "==========   ===========        ===========      =========        =========")
	for symbol, stock in stocks.items():
		print(f'{symbol:<10}   {stock[0]:11}        {stock[1]:>11.2f}      {stock[2]:>9.2f}         {stock[1] * stock[2]:>8.2f}')
	
	total = 0
	for value in stocks.values():
		total = total + value[1]*value[2]
	print(f'TOTAL: {total:>68.2f}')

	
# Enables the user to buy stock/s
def buyStock(stocks):
	print("======BUY STOCK======")
	get_symb = input("Enter symbol: ").upper()
	if get_symb != "CASH":
		if get_symb in stocks:
			print("Adding more shares of", get_symb)
		else:
			print("INFO: Initial entry of", get_symb)
			ent_desc = (input("Enter Company Name: "))

		ent_qty = float(input("Enter # of shares to buy: "))
		ent_price = float(input("Enter current price per share: "))

		total_value = ent_qty*ent_price

		if total_value > stocks["CASH"][1]*stocks["CASH"][2]:
			print("ERROR: Not enough cash.")
			return stocks
		else:
			print("INFO:", ent_qty, "share/s of", get_symb, "purchased for total", total_value)
			if get_symb in stocks:
				old_qty = stocks[get_symb][1]
				stocks[get_symb] = [stocks[get_symb][0], ent_qty+old_qty, ent_price]
				stocks["CASH"] = [stocks["CASH"][0], stocks["CASH"][1]-total_value, stocks["CASH"][2]]
			else:
				stocks[get_symb] = [ent_desc, ent_qty, ent_price]
				stocks["CASH"] = [stocks["CASH"][0], stocks["CASH"][1]-total_value, stocks["CASH"][2]]
			return stocks
	else:
		print("ERROR: You cannot buy cash.")
		return stocks
	

# Enables the user to sell stock/s
def sellStock(stocks):
	print("======SELL STOCK======")
	there_exists_stock = False
	for key, value in stocks.items():
		if key == "CASH":
			continue
		elif value[1] == 0:
			continue
		else:
			there_exists_stock = True

	if there_exists_stock == False:
		print("ERROR: No stock assets to sell.")
		return stocks
		
	get_symb = input("Enter symbol: ").upper()
	if get_symb not in stocks:
		print("ERROR:", get_symb, "not in portfolio")
		return stocks
	elif get_symb == "CASH":
		print("ERROR: You cannot sell cash")
		return stocks
	else:
		ent_qty = float(input("Enter # of shares to sell: "))
		if ent_qty > stocks[get_symb][1]:
			print("ERROR: Not enough shares")
			return stocks
		else: 
			ent_price = float(input("Enter current price per share: "))

			total_value = ent_qty*ent_price

			print("INFO:", ent_qty, "share/s of", get_symb, "sold for total", total_value)
			stocks[get_symb] = [stocks[get_symb][0], stocks[get_symb][1] - ent_qty, ent_price]
			stocks["CASH"] = [stocks["CASH"][0], stocks["CASH"][1]+total_value, stocks["CASH"][2]]

			

			return stocks


# Enables the user to change the price of a stock		
def changePrice(stocks):
	print("======CHANGE PRICE======")
	there_exists_stock = False
	for key, value in stocks.items():
		if key == "CASH":
			continue
		elif value[1] == 0:
			continue
		else:
			there_exists_stock = True

	if there_exists_stock == False:
		print("ERROR: No stock assets to change")
		return stocks
	
	
	get_symb = input("Enter symbol: ").upper()
	if get_symb not in stocks:
		print("ERROR:", get_symb, "not in portfolio")
		return stocks
	elif get_symb == "CASH":
		print("ERROR: You cannot change the current price of cash")
		return stocks
	elif get_symb not in stocks:
		print("ERROR:", get_symb, "has no shares")
		return stocks
	else: 
		ent_price = float(input("Enter current price per share: "))
		new_price = ent_price

		print("INFO: Current price for", get_symb, "updated to", new_price)
		stocks[get_symb] = [stocks[get_symb][0], stocks[get_symb][1], new_price]
		stocks["CASH"] = [stocks["CASH"][0], stocks["CASH"][1], stocks["CASH"][2],new_price]	
		return stocks
	

# Enables the user to sell all/liquidate all stocks
def sellAll(stocks):
	print("======LIQUIFIED ALL STOCKS======")
	there_exists_stock = False
	for key, value in stocks.items():
		if key == "CASH":
			continue
		elif value[1] == 0:
			continue
		else:
			there_exists_stock = True

	if there_exists_stock == False:
		print("ERROR: No stock assets to liquidate.")
		return stocks
	
	sell_all = input("Are you sure you want to sell all your stocks? Type [Y] to confirm: ").upper()

	if sell_all == "Y":	
		for key,value in stocks.items():
			if key != "CASH" and stocks["CASH"][0] != 0:

				print("INFO: Sold", value[1], "shares of", key,"for total of",value[1]*value[2])

				stocks["CASH"][1] = stocks["CASH"][1] + value[1]*value[2]
				stocks[key][1] = 0
	else:
		print("No action done!")

	return stocks



# Main program loop
STARTING = True
while STARTING:
	print(stocks)
	option = menu()
	if option == 1:
		viewPortfolio(stocks)
	
	elif option == 2:
		stocks = buyStock(stocks)
	
	elif option == 3:
		stocks = sellStock(stocks)

	elif option == 4:
		stocks = changePrice(stocks)
	
	elif option == 5:
		stocks = sellAll(stocks)

	elif option == 6:
		stocks = Tiamzon_ex7_files.loadPortfolio(stocks)

	elif option == 7:
		stocks = Tiamzon_ex7_files.savePortfolio(stocks)

	elif option == 0:
		STARTING = False
		print("Bye!....")

	else:
		print("Invalid Option")
