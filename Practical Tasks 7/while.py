
'''This code will ask you to input numbers. The programme will calculate the average of the number you have entered.
end the programme by enter "-1". (-1 will not be calculated in the average)'''
entry_number = 0
total_sum = 0
user_number = 0

while True:
    user_number = int(input("Please enter a number. (End loop with -1)"))
    if user_number == -1: #use if statement to avoid the loop run again when "-1" is entered
        break
    else:
        entry_number += 1
        total_sum += user_number
        continue

if entry_number != 0:
    average = total_sum/entry_number
    print(average)
else:
    print("Average cannot be calculated.")

