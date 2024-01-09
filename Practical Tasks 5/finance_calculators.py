import math

#this part explain the choices to audience and ask user for input.
print("\nInvestment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed\n")

#if the user choose investment, ask for several variables
if choice.lower() == "investment":
    deposit = float(input("Please enter the amount you want to deposit:"))
    interest_rate = float(input("What is the interest rate in percentage? (Numbers only)"))/100
    number_of_years = float(input("What is the number of years you plan on investing?"))
    interest = input("Please enter if you want 'simple' or 'compound' interest:")
    #depend on whether it is simple or compound interest, calculate and display
    if interest.lower() == "simple":
        simple_interest = (deposit*(1+interest_rate*number_of_years))
        print(f"Your simple interest of £{int(deposit)} after {int(number_of_years)} years will be £{round(simple_interest,2)}.")
    elif interest.lower() == "compound":
        compound_interest = (deposit * math.pow((1+interest_rate),number_of_years))
        print(f"Your compound interest of £{int(deposit)} after {int(number_of_years)} years will be £{round(compound_interest,2)}.") 
    else:
        print("Sorry I didn't understand.")
#if user choose bond, ask for essential numbers:
elif choice.lower() == "bond":
    house_value = float(input("Please enter the value of the house.(e.g.100000):"))
    interest_rate = float(input("What is the interest rate in percentage? (Numbers only)"))/100/12
    number_of_months = float(input("Please enter the months you will take to repay the bond:"))
    #calculate and display repayment
    repayment = (house_value*interest_rate)/(1-(1+interest_rate)**(-number_of_months))
    print(f"You will need to pay £{round(repayment,2)} each month.")
else:
    print("Sorry, I didn't understand your choice.")