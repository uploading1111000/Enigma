"""from machine.machineInstance import *
w = input("Wheelorder: ")
rs = input("Ring numbers: ")
pb = input("Plugboard: ")
rp = input("Key: ")
m = machineInstance(wheelorder = w, ringposition = rs, rotorposition = rp, plugboard = pb)
while True:
    print(m.encryptText(input("Text: ")))"""
import solver.analysis
#solver.analysis.depreface("src/solver/english",r"\*\*\* ?START OF (THE|THIS) PROJECT GUTENBERG EBOOK [\S ]* ?\*\*\* *")
#solver.analysis.makeEngimable("src/solver/english")
solver.analysis.collect("src/solver/english")