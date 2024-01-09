import math  #import math module

side1 = input("Please enter a length of triangle side in integer:")
side2 = input("Please enter a second length of triangle side in integer:")
side3 = input("Please enter a third length of triangle side in integer:")

int_side1 = int(side1)
int_side2 = int(side2)
int_side3 = int(side3)

s = (int_side1 + int_side2 + int_side3)/2
#print(s)

area = math.sqrt(s*(s-int_side1)*(s-int_side2)*(s-int_side3))
print(area)