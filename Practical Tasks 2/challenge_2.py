string_fav = input("Please enter your favourate reseraunt name:")
int_fav = int(input("Please enter your favourate number"))
print(int(string_fav))
print(int(int_fav))

''' When use int for a string, it shows a value error: invalid literal for int()
with base 10. I think because the system canot recognize the letters in an int()
casting.'''
