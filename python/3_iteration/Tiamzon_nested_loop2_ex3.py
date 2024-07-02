# This program will print a boxed "X" and unboxed "X"
# Created by: Edgar Alan Emmanuel B. Tiamzon III
# 09-26-23

# Get inputs
dim = input("Enter a dimension: ")
dim = int(dim)

#Draw square
col = 0 #initialize

#Printing box "X" and unboxed "X"
while col < dim:
	row = 0
	while row < dim:
		if (row == dim-1) or (col == row) or (col == dim) or (col == dim-1) or (col == dim+1) or (row == dim+1) or (col == 0) or (row == 0) or (col == dim-(row+1)):
			print("* ",end="")
		else:
			print(" ",end=" ")
	
		row = row +1 #increment
	print() # print new line at the end of row
	col = col + 1 #increment
	
print()

col = 0	
	
while col < dim:
	row = 0		
	while row < dim:
		if (row + col == dim-1) or (col == row):
			print("* ",end="")
		else:
			print(" ",end=" ")
			
	
		row = row +1 #increment
	print() # print new line at the end of row
	col = col + 1 #increment
