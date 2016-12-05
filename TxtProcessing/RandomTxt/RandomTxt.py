import string
import random
import time

# This is the set of all the characters that can be used
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

# the target text that can be used
target = input("Enter your target text: ")
# This is used to generate all the generation of text
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attemptNext = ''

completed = False

generation = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched! That took " + str(generation) + " generation(s)")
