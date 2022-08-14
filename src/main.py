"""from machine.machineInstance import *
w = input("Wheelorder: ")
rs = input("Ring numbers: ")
pb = input("Plugboard: ")
rp = input("Key: ")
m = machineInstance(wheelorder = w, ringposition = rs, rotorposition = rp, plugboard = pb)
while True:
    print(m.encryptText(input("Text: ")))"""
import solver.analysis
solver.analysis.depreface("src/solver/deutsch",r"\*\*\* ?START OF (THE|THIS) PROJECT GUTENBERG EBOOK [\S ]* ?\*\*\* *")