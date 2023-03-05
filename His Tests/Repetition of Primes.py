# Help used:
'''
https://www.geeksforgeeks.org/python-program-to-check-prime-number/
https://pythonsolved.com/how-to-find-prime-numbers-in-range-in-python/#:~:text=To%20find%20prime%20numbers%20in%20the%20range%20in,passing%20each%20value%20to%20the%20is_prime%20%28%29%20function.
Help your kids with MATHS: pg 26 - 27
'''

# Main instructions
'''
* Create a program that prints messages for 100 times
* In numerical order:
    * Make numerically prime messages "Good luck!"
    * Make the rest "Happy New Year!"
'''

for messange_count in range(101): # Counts the order of messanges

    # For special cases
    if messange_count == 0:
        continue # Skip 0
    elif messange_count == 1: # 1 is neither composite or prime
        print(messange_count, "???")

    # Rest of the possible numbers
        # If messange_count == 2, 3, 5, or 7, then messange_count is prime
    elif messange_count == 2:
        print(messange_count, "Good luck!")
    elif messange_count == 3:
        print(messange_count, "Good luck!")
    elif messange_count == 5:
        print(messange_count, "Good luck!")
    elif messange_count == 7:
        print(messange_count, "Good luck!")

        # If messange_count leaves no remainders when dividing with certain numbers, it is divisible, so it is composite
    elif messange_count % 2 == 0: # Finds if no remainders can be found when dividing, which checks its divisibility
        print(messange_count, "Happy New Year!")
    elif messange_count % 3 == 0: # Finds if no remainders can be found when dividing, which checks its divisibility
        print(messange_count, "Happy New Year!")
    elif messange_count % 5 == 0: # Finds if no remainders can be found when dividing, which checks its divisibility
        print(messange_count, "Happy New Year!")
    elif messange_count % 7 == 0: # Finds if no remainders can be found when dividing, which checks its divisibility
        print(messange_count, "Happy New Year!")

    # If there is only remainders, it is prime
    else:
        print(messange_count, "Good luck!") # If none of those numbers are divisible, then it is prime
        continue # Skip