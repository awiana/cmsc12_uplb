# This program will create a persistance on the portfolio tracking system in order for the user/investor to keep his/her cash and stocks assets portfolio information
# Created by: Edgar Alan Emmanuel B. Tiamzon III
# B1L
# 10/24/23


def loadPortfolio(stocks): # enables to loads/refreshes the user's cash and stock assets from its portfolio information 
	print("======PORTFOLIO======")
	load_port = open("portfolio.dat","r")

	lists = []

	for line in load_port:
		data = line.rstrip("\n").split(",")
		lists.append(data)


	stocks = {
		 "CASH" : ["Cash", float(lists[0][1]), 1.00]
		}

	for i in range(len(lists)):
		get_symb = ""
		ent_desc = ""
		ent_qty = 0
		ent_price = 0
		if i != 0:
			get_symb = lists[i][0]
			ent_desc = lists[i][1]
			ent_qty = float(lists[i][2])
			ent_price = float(lists[i][3])

		stocks[get_symb] = [ent_desc, ent_qty, ent_price]
		

	load_port.close()

	return stocks		


def savePortfolio(stocks): # enables to save cash and stock assets portfolio information
	save_port = open("portfolio.dat","w")
	cash_amt = "CASH" + "," + str(stocks["CASH"][1])
	save_port.write(cash_amt + "\n")

	for key,value in stocks.items():
		if key != "CASH": 
			get_symb = key
			ent_desc = value[0]
			ent_qty = round(value[1], 2 )
			ent_price = round(value[2], 2)
			data = key + "," + str(ent_desc) + "," + str(ent_qty) + "," + str(ent_price)
			save_port.write(data + "\n")

	save_port.close()

	print("\n======SAVE PORTFOLIO======")
	print("\nINFO: Sucessfully saved portfolio information")
