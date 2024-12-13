
date = input('Input a date following the example - 2024.11.15: ')

print(f'Der Typ von date ist: {type(date)}')

if date < '2024.11.25':
    print(f'The course has not started yet'),
elif date == '2024.11.25':
    print(f'The beginning of the course'),
elif date >= '2024.12.23' and date <= '2025.01.02':
    print('Christmas vacations'),
elif date == '2025.02.25':
    print(f'The end on Module 1'),
else: 
    print('A normal day of the course')
