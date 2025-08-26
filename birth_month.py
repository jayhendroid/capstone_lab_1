# Part 1: Hello, birthday month - variable and if-statements
#
# Write a program that asks for your name and the month you were born in.
#
# Then, your program should print
# A greeting to you, using your name
# A message with the number of letters in your name
# A 'Happy birthday month!' message if you were born in the current month
# Easier - compare the user's input to "January" or "August" or whatever the current month is
# Harder - use Python to figure out the current month and use that in the comparison. Check out the datetime library.

name = input('Hello, please enter your name: ')
birth_month = input('Please enter your birth month: ')

print(f'Hello {name}')


letters_in_name = len(name)

print(f'You have + {letters_in_name} + letters in your name')

if birth_month.lower() == 'august':
    print('Happy birthday month!!!')
else:
    print('it is not your birthday month')

