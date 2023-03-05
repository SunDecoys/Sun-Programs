# Video: https://www.youtube.com/watch?v=KFVdHDMcepw&t=6s

'''
Instructions:

* The only way to get out of the prison is to open a lock.
* The lock has a dial that can be spun to 100 different positions.
    * Ranged from 1 to 100
* Only 1 out of the set 100 positions can make the lock open.
* The lock is red when it is locked, and green when it is unlocked.
    * Hedge can only see the color of the lock to tell if the lock is opened or closed.
'''

import random
lock = [random.randint(1, 100), 1, "Red"] # [Dial's position that unlocks lock, current position of dial, current color of lock]
# lock[0]: A random number generator from 1 to 100. The chosen interger represents the dial's position that unlocks the lock.
# lock[1]: The current position of the lock's dial, set at 1.
# lock[2]: The color of the lock represents the locked and unlocked states of the lock. It is currently red because it is locked.


while lock[2] == "Red": # While Hedge sees the lock as the color red.

    if lock[1] == lock[0]: # Is the current positon of the lock, the position that unlocks the lock?
        lock[2] = "Green" # If yes, the lock is unlocked, and the lock becomes green.
        print("SUCCESS : At dial position", lock[1], ", Lock is now", lock[2], ".") # Shown output.

    else: # If not, the lock is still locked.
        print("FAILURE : At dial position", lock[1], ", Lock is still", lock[2], ".") # Shown output.
        lock[1] += 1 # Hedge turns the dial to the next position, and checks the color of the lock again.

'''
What I learned:
    * Iterate in programming means to repeat.
    * Until loops are loops that iterate until a condition is met.

What I did well:
    * (One of) the most efficient algorithm(s) (as explained in the episode).
    * Clear comments.
    * Easy to understand.

What I can improve on:
    * Using seperate variables/identifiers to store lists, instead of using indexes in lists.
    As it makes identifying values easier due to their unique names.
'''