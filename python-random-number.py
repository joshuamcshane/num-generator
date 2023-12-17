import random

#prompt user for input
number_of_digits = input("How many digits do you want in your random string?\n")

#convert input string to digits
number_of_digits_int = int(number_of_digits)

#empty string to add digits
output = ""

#index
i = 0

#generate a random digit and append it to the string. Repeat until we hit the number the user specified.
while i < number_of_digits_int:
    output += str(random.randint(0,9))
    i += 1

#return digits
print(output)