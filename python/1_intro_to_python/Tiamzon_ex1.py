# This program will compute the amount you spend on milk tea per year
# Created by: Edgar Alan Emmanuel B. Tiamzon III

# Make the given variable constant
r = 0.04
T = 52

# Ask for the output
P = input('\nHow many times in a week you buy a milk tea? ')
P = int(P)

# Ask for the output
M = input('How much is the cost of the milktea? ')
M = int(M)

# Do the computation
PMT = (P*M*T)

# Display the total amount will spend on milk tea per year PMT
print("\n")
print('The total amount you will spend on milk tea per year is ',int(PMT),'.',sep="")
print("\n")


# Ask for the output
print("If you save this money every year in a high-yield bank account earning 4% APY, you would have earned an extra: ")

# Do the computation 
FV1 = PMT*((((1 + r)**1) - 1)/r)
FV5 = PMT*((((1 + r)**5) - 1)/r)
FV10 = PMT*((((1 + r)**10) - 1)/r)
FV20 = PMT*((((1 + r)**20) - 1)/r)
FV40 = PMT*((((1 + r)**40) - 1)/r)	

PMT5 = (P*M*T)*5
PMT10=(P*M*T)*10
PMT20 = (P*M*T)*20
PMT40= (P*M*T)*40



print("Php ",int(FV1), "in 1 year (vs. spending Php ",int(PMT),")",sep = '')
print("Php ",int(FV5), "in 5 year (vs. spending Php ",int(PMT5),")",sep = '')
print("Php ",int(FV10),"in 10year (vs. spending Php ",int(PMT10),")",sep = '')
print("Php ",int(FV20),"in 20year (vs. spending Php ",int(PMT20),")",sep = '')
print("Php ",int(FV40),"in 40year (vs. spending Php ",int(PMT40),")\n",sep = '')
