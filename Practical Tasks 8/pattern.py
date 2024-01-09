'''The following programe will print out a pattern.
The range 1 to 10 constrain the number of rolls to 9.
If the number in range 1-10 is smaller or equals to 5, print the according number of "*" to construct the ascending part.
If the number in range 1-10 is larger than 5, print the "*" according the 10 minus the number for the descending part.'''
for num in range(1,10):
    if num <= 5:
        print("*"*num)
    else:
        print("*"*(10-num))