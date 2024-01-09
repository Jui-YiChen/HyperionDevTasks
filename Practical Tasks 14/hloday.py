#This task is designed to calculate the user's holiday cost. Including plane cost, hotel cost, and car-rental cost.

#Show the flight information and ask about the detail of destination, days in hotel and car-rental.
print('''
Flight Ticket Price from London(£):
New York: 1000
Taiwan: 750
Malaysia: 680
Korea: 800\n''')

city_flight = input("Which city are you flying to?\n").strip().lower()
num_night = int(input("How many nights are you planning to stay there?\n"))
rental_days = int(input("How many days are you planning to rent a car?\n"))

#Store the ticket price in a dictionary
ticket_price={
    "new york":1000,
    "taiwan":750,
    "malaysia":680,
    "korea":800
}

#Create a personalised function for total cost
def cost_calculation(number_of_days, cost_per_day):
    total = number_of_days*cost_per_day
    return total

#Calculate the price for hotel, flight and car
hotel_cost = cost_calculation(num_night, 200)

for key, values in ticket_price.items():
    if city_flight == key:
        flight_cost = values

car_cost = cost_calculation(rental_days,50)

total_cost = hotel_cost+flight_cost+car_cost

print(f"Your hotel cost will be £{hotel_cost}, your flight cost will be £{flight_cost}, and your car-rental cost will be £{car_cost}.")
print(f"Your total cost will be £{total_cost}.")