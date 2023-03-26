# Make it solve any two step equation in this format:
# ax+b=c

while True:
    print('''
Welcome, I can solve any kind of two step equation in this format:

    a x + b = c     *Let x be the unknown variable.

**DO NOT ENTER letters or other symbols, only numbers.
''')

    while True:
        print('''Now, what will the value for a be?''')
        a = input("a = ")

        print('''
Now, what will the value for b be?''')
        b = input("b = ")

        print('''
Now, what will the value for c be?''')
        c = input("c = ")

        if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
            print('''
ERROR, please enter numbers only.
''')

        else:
            a = int(a)
            b = int(b)
            c = int(c)
            break

    print(f'''
Thank you, I will now convert this equation into a solved one.


Unsolved equation:
a x + b = c

Substituting known variables:
{a} x + {b} = {c}

Subtracting {b} from both sides:
{a} x ( + {b} - {b} ) = {c} - {b}

Simplifying expression:
{a} x = {c - b}

Dividing {a} from both sides:
{a} / {a} x = {c - b} / {a}

Simplifying expression:
x = {(c - b) / a}

EQUATION SOLVED:


Now, do you want to use the program again, or do you want to stop it?

    enter "y" continue, "n" for stop

*CASE SENSITIVE, INPUT IN MINISCULE CASE, INPUT ONLY THE CHARACTERS "y" or "n" ''')
    while True:
        continueProgram = input("continueProgram = ")

        if continueProgram == "y" or continueProgram == "n":
            break

        else:
            print('''
ERROR, please enter either "y" or "n" in miniscule case.''')

    if continueProgram == "n":
        break