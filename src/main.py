"""from machine.machineInstance import *
w = input("Wheelorder: ")
rs = input("Ring numbers: ")
pb = input("Plugboard: ")
rp = input("Key: ")
m = machineInstance(wheelorder = w, ringposition = rs, rotorposition = rp, plugboard = pb)
while True:
    print(m.encryptText(input("Text: ")))"""
import solver.fitnessFunctions
import testing.fitnessTests
testing.fitnessTests.testFuncSimple(solver.fitnessFunctions.indexCoincidence)
testing.fitnessTests.testFuncSimple(solver.fitnessFunctions.nGramScore,1)
testing.fitnessTests.testFuncSimple(solver.fitnessFunctions.nGramScore,2)
testing.fitnessTests.testFuncSimple(solver.fitnessFunctions.nGramScore,3)
