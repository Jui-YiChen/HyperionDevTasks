def calculate_total_time(swimming_time, cycling_time, running_time):
    return swimming_time + cycling_time + running_time

def determine_award(total_time):
    qualifying_time = 100

    if total_time <= qualifying_time:
        return "Provincial Colours"
    elif qualifying_time < total_time <= qualifying_time + 5:
        return "Provincial Half Colours"
    elif qualifying_time + 5 < total_time <= qualifying_time + 10:
        return "Provincial Scroll"
    else:
        return "No award"

def main():
    try:
        swimming_time = float(input("Enter swimming time (in minutes): "))
        cycling_time = float(input("Enter cycling time (in minutes): "))
        running_time = float(input("Enter running time (in minutes): "))

        total_time = calculate_total_time(swimming_time, cycling_time, running_time)
        
        print(f"\nTotal time for the triathlon: {total_time:.2f} minutes")
        
        award = determine_award(total_time)
        print(f"Award: {award}")

    except ValueError:
        print("Please enter valid numerical values for the times.")

if __name__ == "__main__":
    main()
