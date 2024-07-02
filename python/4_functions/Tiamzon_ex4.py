# This program will create a security PIN in order to unlock the secret message
# Edgar Alan Emmanuel B. Tiamzon III
# 10/03/23

securityPIN = None
MESSAGE = "You'll succeed in life and will reach your goal! Heads up!"

# Build menu
def menu(securityPIN):
	exited = True
	while exited:
		if (securityPIN == None):
			securityPIN = input("Enter your PIN: ")
			print("Your PIN has been successfully entered")
			exited = False
		else: 
			pin = input("Enter a PIN: ")
			if (pin == securityPIN):
				print("Change your current PIN")
				exited = True
			else:
				print("Incorrect PIN!")
				exited = False
			return securityPIN
		
# MAIN MENU (No parameters, returns an integer)
def menu():
	print("::::::::::::MENU::::::::::::")
	print("[0] Exit program")
	print("[1] Unlock Secret Message")
	print("[2] Change Security PIN")
	print("::::::::::::::::::::::::::::")
	
	# Get the choice from the user
	choice = int(input("Input choice: "))
	return choice

# Define the secret message function
def secret_message(securityPIN):
	exited = False
	while not exited:
		if (securityPIN is None):
			securityPIN = manage_pin(securityPIN)
			exited = True
		else:
			pin = input("Enter your PIN: ")
			if (pin == securityPIN):
				print(MESSAGE)
				exited = True
			else:
				print("Incorrect PIN!")
				exited = True
	return securityPIN

# Define the manage PIN function
def manage_pin(securityPIN):
	exited = False
	while not exited:
		if (securityPIN is None):
			pin = input("Enter a new PIN: ")
			if not len(pin) == 4 or not pin.isalnum():
				print("Invalid PIN!")
				exited = True
			else:
				securityPIN = pin
				print("Your PIN has been successfully entered")
				exited = True
		else:
			pin = input("Enter your PIN: ")
			if pin == securityPIN:
				pin = input("Enter a new PIN: ")
				if not len(pin) == 4 or not pin.isalnum():
					print("Invalid PIN!")   
					exited = True
				else:
					securityPIN = pin
					print("Your PIN has been successfully entered")
					exited = True
	return securityPIN

exited = False
while not exited:
	choice = menu()
	if (choice == 0):
		print("Bye!")
		exited = True
	elif (choice == 1):
		securityPIN = secret_message(securityPIN)
	elif (choice == 2):
		securityPIN = manage_pin(securityPIN)
	else:
		print("Invalid choice")
