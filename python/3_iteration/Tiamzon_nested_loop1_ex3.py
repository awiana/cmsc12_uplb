# This program daws a transparent square
# Created by: Edgar Alan Emmanuel B. Tiamzon III
# 09-26-23

# Get inputs
dim = input("Enter a dimension: ")
dim = int(dim)

#Draw square
col = 0 #initialize

#Printing hollow star in right triangle
while col < dim:
	row = 0
	while row < dim:
		if (row == 0) or (col == row) or (col == dim) or (col == dim-1):
			print("* ",end="")
		else:
			print(" ",end=" ")
		
		row = row +1 #increment
	print() # print new line at the end of row
	col = col + 1 #increment
		
