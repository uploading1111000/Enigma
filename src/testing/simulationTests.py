from machine.machineSimulate import simulateFull, simulateWords
import random
import copy
def test():
    t = 0
    while t < 26 ** 3:
        t+=1
        string = [random.randint(0,25) for x in range(random.randint(0,10))]
        wheelOrder = random.sample(range(8),3)
        rotorpositions = [random.randint(0,25) for x in range(3)]
        ringpositions = [random.randint(0,25) for x in range(3)]
        cString = simulateFull(string,wheelOrder,copy.deepcopy(rotorpositions),ringpositions)
        pString = simulateFull(cString,wheelOrder,copy.deepcopy(rotorpositions),ringpositions)
        if pString != string:
            print([chr(x+65) for x in string])
            print([chr(x+65) for x in cString])
            print([chr(x+65) for x in pString])
            print([x + 1 for x in wheelOrder])
            print([x + 1 for x in wheelOrder])
            print([chr(x+65)for x in rotorpositions])
            print(ringpositions)
            print(t)
            break
