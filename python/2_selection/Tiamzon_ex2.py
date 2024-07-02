# This program will help the students in deciding which establishment they could eat in their lunch time
# Create by: Edgar Alan Emmanuel B. Tiamzon III 
# Student Num: 2023-15128
# Date: 09-19-23

# Recommended establishment
# Where you want to eat?
establishment = input("Hello! What type of establishment you would like to eat at? (RESTAURANT, FAST FOOD, HOMEMADE)? ") 
establishment = establishment.upper()


# Recommended Establishment for students
if (establishment == "RESTAURANT") or (establishment == "FAST FOOD") or (establishment == "HOMEMADE"):

# Ask the students on how many there are in the group
	group = int(input("Can I ask how many are you in the group? "))


else: 
	print("This type of establishment is not invalid.")
	exit()
	
# This line will run the program considering the input of establishment and group
if (establishment == "RESTAURANT"):
	if (group >= 1) and (group <= 3):
		print("Based on the number you are with, I recommend you to eat at Dalcielo!")
	elif (group<1):
		print("Sorry! this is an invalid input!")
	else:
		print("Based on the number you are with, I recommend you to eat at Bonitos!")

elif (establishment == "FAST FOOD"):
	if (group >= 1) and (group <= 3):
		print("Based on the number you are with, I recommend you to eat at Mcdonalds!")
	elif (group<1):
		print("Sorry! this is an invalid input!")
	else:
		print("Based on the number you are with, I recommend you to eat at Jollibee!")
		
elif (establishment == "HOMEMADE"):
	if (group >= 1) and (group <= 3):
		print("Based on the number you are with, I recommend you to eat at Aling Glo's!")
	elif (group<1):
		print("Sorry! this is an invalid input!")
	else:
		print("Based on the number you are with, I recommend you to eat at Cadapan's!")
		
