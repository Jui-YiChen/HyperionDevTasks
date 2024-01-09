import math
print(2000*(1+0.08*20))
print(2000*math.pow((1+0.08),20))



import math

# This part explains the choices to the audience and asks the user for input.
print("\nInvestment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed\n")

# If the user chooses investment, ask for several variables
if choice.lower() == "investment":
    deposit = float(input("Please enter the amount you want to deposit:"))
    interest_rate = float(input("What is the interest rate in percentage? (Numbers only)")) / 100
    number_of_years = float(input("What is the number of years you plan on investing?"))
    interest = input("Please enter if you want 'simple' or 'compound' interest:")
    
    if interest.lower() == "simple":
        simple_interest = deposit * (1 + interest_rate * number_of_years)
        print(simple_interest)
    elif interest.lower() == "compound":
        compound_interest = deposit * math.pow((1 + interest_rate), number_of_years)
        print(compound_interest)
    else:
        print("Sorry, I didn't understand.")

# If the user chooses bond:
elif choice.lower() == "bond":
    house_value = float(input("Please enter the value of the house (e.g., 100000):"))
    interest_rate = float(input("What is the interest rate in percentage? (Numbers only)")) / 100
    number_of_months = float(input("Please enter the months you will take to repay the bond:"))
    
    repayment = (interest_rate / 12 * house_value) / (1 - (1 + interest_rate / 12) ** (-number_of_months))
    print(repayment)
else:
    print("Sorry, I didn't understand your choice.")
