# Make it solve any two step equation in this format:
# (a+b)/x=3

while True:
    print('''
Welcome, I can solve any kind of two step equation in this format:

    a + b
    ————— = c   *Let x be the unknown variable.
      x

**DO NOT ENTER letters or other symbols, only numbers.
''')

# STAGE: Input
    while True: # Asks what the values for the variables will be. Values will be in string format.
        print('''Now, what will the value for a be?''')
        a = input("a = ")

        print('''
Now, what will the value for b be?''')
        b = input("b = ")

        print('''
Now, what will the value for c be?''')
        c = input("c = ")

# STAGE: Input
        # STAGE: Input.Numerical?
        if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False: # Checks if the variables contain only numbers.
            print('''
ERROR, please enter numbers only.
''') # If the variables do not have only numbers, ERROR messange will appear, goes back to the next iteration (from "while True:") and asks values again.

# STAGE: Input.Conversion
        else: # If the variables do have only numbers, converts values to intergers so it can be used with math operaters.
            a = int(a) 
            b = int(b)
            c = int(c)
            break # Breaks the loop, instead of asking values again, it moves to 

# STAGE: Output
    print(f'''
Thank you, I will now convert this equation into a solved one.


Unsolved equation:
a + b
————— = c
  x

Substituting known variables:
( {a} + {b} ) / x = {c}

Multiplying x from both sides:
x * ( {a} + {b} ) / x = x {c}

Simplifying expression:
{a} + {b} = x {c}

Dividing {c} from both sides:
({a} + {b}) / {c} = x {c} / {c}

Simplifying expression:
({a} + {b}) / {c} = x

Adding {a} with {b}:
{a + b} / {c} = x

Dividing {a + b} with {c}:
{(a + b) / c} = x

EQUATION SOLVED:


Now, do you want to use the program again, or do you want to stop it?

    enter "y" continue, "n" for stop

*CASE SENSITIVE, INPUT IN MINISCULE CASE, INPUT ONLY THE CHARACTERS "y" or "n" ''')
    while True:
        continueProgram = input("continueProgram = ") # Input that allows the continuation of the program or not.

        if continueProgram == "y" or continueProgram == "n": # Breaks the "while True" loop.
            break

        else: # If inputed incorrectly, enter ERROR messenge and go back to "while True loop", asks for the continuation of the program again.
            print('''
ERROR, please enter either "y" or "n" in miniscule case.''')

    if continueProgram == "n": # If "y", it goes back to the "while True loop" at line 4, reiterating the whole program back to the beginning.
        break                  # If "n", break the cycle of the program. Program Stops.