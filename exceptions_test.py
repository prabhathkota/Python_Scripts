print('Subtraction program, v0.0.3 (beta)')
loop = 1
while loop == 1:
    try:
        a = input('Enter a number to subtract from > ')
        b = input('Enter the number to subtract > ')
        print(int(a) - int(b))  
    except NameError:
        print("\nYou cannot subtract a letter")
        continue
    except SyntaxError:
        print("\nPlease enter a number only.")
        continue
    except ValueError:
        print("\nPlease enter a number only - Value Error.")
        continue
    try:
        loop = input('Press 1 to try again > ')
    except (NameError,SyntaxError,ValueError):
        print("\nInside Error 111") 
        loop = 0