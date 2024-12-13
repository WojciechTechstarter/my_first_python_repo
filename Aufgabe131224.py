# Aufgabe 1

a = input('Input a random number')
b = input('Input another random number')

a_float = float(a)
b_float = float(b)


if a_float > b_float:
    print('a is bigger than b')
elif a_float == b_float:
    print('a is equal to b')
else:
    print('a is smaller than b')


# Aufgabe 2

result_1 = input('Input your test result: ')

result_1_float = float(result_1)

if result_1_float >= 90 and result_1_float <= 100:
    print('Great Work! You get an A!')

elif result_1_float >= 70:
    print('Nicely done! You get a B!')

elif not(result_1_float > (30)):
    print('You did not even try! You get an F!')

else:
    print('You barely made it. You get a C')


# Aufgabe 3

x = 7
y = 3
z = 10

print((x > y and y < z) or not(x))
    
