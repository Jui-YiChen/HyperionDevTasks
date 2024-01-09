
#use range and len to identify the number of characters, use for loop to operate the upper or lower case based on the corresponding index for each character.
sentence = input("Give me a sentence here:")
alt_sentence = ""

for i in range(len(sentence)):
    if i % 2 == 0:
        alt_sentence += sentence[i].upper()
    else:
        alt_sentence += sentence[i].lower()

print(alt_sentence)


#split the sentense into multiple strings by space
#create an empty list, if the string in the list is at index 0,2,4,6: add to the list in upper case
#if the string in list is at index 1,3,5,7: add to list in lower case.
#print out the list by joining all the strings using space
split_sentence = sentence.split(" ")
alt_word = []

for i in range(len(split_sentence)):
    if i % 2 == 0:
        alt_word.append(str(split_sentence[i]).upper())
    else:
        alt_word.append(str(split_sentence[i]).lower())

print(" ".join(alt_word))
