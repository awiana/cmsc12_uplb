# This program will draw letter C by indicating the entered dimension from the user
# Created by: Edgar Alan Emmanuel B. Tiamzon III
# Date: 09-26-23

# Get the input of dimension
dim = input("Enter a dimension: ")
dim = int(dim)

# Draw letter C
row = 0 #initialize

#Printing letter C
while row < dim:
	col = 0 # assign
	while col < dim:
		if (row == 0 or row == dim-1) or (col == 0 or col == dim-0):
			print("* ", end="")
		else: 
			print("  ", end="")
			
		col = col + 1 #increment
	print() # print new line at the end of row
	row = row +1 #increment
