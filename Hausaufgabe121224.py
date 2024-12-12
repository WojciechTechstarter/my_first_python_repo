
### 1. Hausaufgabe
# collecting data

first_name = input('Please type in your first name')
surname = input('Please type in your last name')

# displaying first name and last name

print(f'Your first name is: {first_name} and your surname is: {surname}')


### 2. Hausaufgabe

# collecting data

number1 = input('Input the first number')
number2 = input('Input the second number')

# changing the data to numbers (either int or float, where float is a more versitale option)

number1 = float(number1)
number2 = float(number2)

# Calculating the sum of the numbers

sum = number1 + number2

# displaying the result

print(f'The sum of the given numbers is: {sum}')

### Hausaufgabe 3
# Write a program that shows if the user's input number is positive, negative or null.

# Collecting data

number3 = input('Input a random number')

# changing the data to numbers

number3 = float(number3)

# Writing an if statement

if number3 == 0:
    print('The number is equal to 0')

elif number3 > 0:
    print('The number is positive')

else:
    print('The number is negative')