import random 
number = (random.randint(0,10))

player_name = input("enter your name")
number_of_guess = 0
print('let\'s play '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guess < 3:
    guess = int(input())
    number_of_guess += 1
    if guess < number:
        print ('Your number is too low')
    if guess > number:
        print  ('Your number is too high')
    if guess == number:
        break
    if guess == number:
        print('You guess the number in a number of' + " " + str(number_of_guess) + " " + 'tries')
    else:
        print('You didn\'t guess the number in a number of' + " " + str(number_of_guess) + " " + 'tries')


