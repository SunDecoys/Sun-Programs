# Main instructions
'''
* Create a program that prints messages for 100 times
* In numerical order:
    * Make numerically odd messages "Good luck!"
    * Make numerically even messages "Happy New Year!"
* Now use a function
'''

def odd_and_even_check():
    if messenge_count % 2 == 0 and messenge_count != 0:
        print(messenge_count, "Happy New Year!")
    elif messenge_count != 0:
        print(messenge_count, "Good luck!")

for messenge_count in range(101): # Counts the order of messanges counting from 0 to 100
    odd_and_even_check()