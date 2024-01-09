str_manip = input("Please enter a sentence:") #ask user to enter a sentense and store in a variable
#print(str_manip)

str_len = len(str_manip) #measure the length of string entered
#print(str_len)

'''
last_word = str_manip[-1] #identify the last word of the string
print(last_word)

replace_str_manip = str_manip.replace(last_word,"@") #replace last word with "@"
print(replace_str_manip)
'''

replace_str_manip = str_manip.replace(str_manip[-1],"@") #replace last word with "@"
print(replace_str_manip)

print(str_manip[:-4:-1]) #print last three letters backward

print(str_manip[:3]+str_manip[-2:]) #print the first three letter and last two letters