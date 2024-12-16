
date = input('Input a date following the example - YYYY.MM.DD: ')

print(f'The filetype is: {type(date)}')

if date < '2024.11.25':
    print(f'The course has not started yet'),
elif date == '2024.11.25':
    print(f'The beginning of the course'),
elif date >= '2024.12.23' and date <= '2025.01.02':
    print('Christmas vacations'),
elif date == '2025.02.25':
    print(f'The end of Module 1'),
elif date > '2025.11.25':
    print(f'The course has ended')
else: 
    print('A normal day of the course')
