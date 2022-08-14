from ..machine.machineSimulate import simulateFull
from fitnessFunctions import nGramScore, indexCoincidence

#note: i want to redesign the entire settings selection system. allow different machines to be simulated and solved and not just have to check every possible machine
def solveSingle(ciphertext):
    rotorSettings = findOptimumRotorSettings(ciphertext,1000)
    ringRotorSettings = findOptimumRingSettings(ciphertext, rotorSettings, 100)          #This is pseudocode
    settingsSuite = hillClimbPlugs(ciphertext,ringRotorSettings, 10)
    return simulateFull(ciphertext,settingsSuite)

#REFACTOR THE SETTINGS SYSTEM TO USE CLASSES? - bid you goodnight
