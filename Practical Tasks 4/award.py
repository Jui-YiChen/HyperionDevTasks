swim_time = int(input("Enter the time to complete swimming in minute:")) #request input of time
cycle_time = int(input("Enter the time to complete cycling in minute:"))
run_time = int(input("Enter the time to complete running in minute:"))

total_time = swim_time+cycle_time+run_time #calculate total time spend
print("Total time = " + str(total_time) + " minutes.") #display total time


if 0 <= total_time <= 100:
    print("Congrats! You have earned a Provincial Colours Award!") # 0-100 award
elif 100 < total_time <= 105:
    print("Congrats! You have earned a Provincial Half Colours Award!") #100-105 award
elif 105 < total_time <= 110:
    print("Congrats! You have earned a Provincial Scroll Award!") #105-110 award
else:
    print("Sorry, you didn't get any award.")