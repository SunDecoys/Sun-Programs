# Video: https://www.youtube.com/watch?v=axBuiB55CfA&list=PLJicmE8fK0EiFngx7wBddZDzxogj-shyW&index=2

'''
Instructions:

* You must find a leader of a resistance group. The only information about the person is this:
    * They have green eyes
    * If the leader has red hair, their name has consecutive double letter
    * If the leader has glasses, their name has 2 vowels
    * If the leader does not wear glasses, their name has 3 vowels
    * There is only one person that matches all of the descriptons
'''
''' Keep this for now
# personWhatever = [eyeColour, hairColour, wearingGlasses?, Name]
personA = ["black", "white" False, "doubleLetter"]
personB = ["blue", "bald", True, "twoVowels"]
personC = ["green", "red", False, "threeVowels"]
'''

import random
def person():
    
    eyeColour = random.choice(["Red", "Brown", "Green"])
    hairColour = random.choice(["Black", "Gray", "Red"])
    isWearingGlasses = random.choice([False, True])
    name = random.choice(["Aaron", "Abby", "Bob", "Jack"])

    return eyeColour, hairColour, isWearingGlasses, name

person()

personWhatever = [eyeColour, hairColour, isWearingGlasses, name]
print(name)