number = 23
running = True

while running:
    try:
        guess = int(input('Enter an integer : '))
        if guess == number:
            print('Congratulations, you guessed it.')
            running = False # this causes the while loop to stop
        elif guess < number:
            print('No, it is a little higher than that.')
        else:
            print('No, it is a little lower than that.')
    except ValueError:
        print("\nPlease enter a number only - Value Error.")
        continue        
else:   #There is else for While loop as well 
    print('The while loop is over.')
    # Do anything else you want to do here

print('Done')