from machine.machineSimulate import simulateFull, simulateStd, simulateWords, simulateNumber
from machine.conversions import *
class machineInstance:
    def __init__(self, **kwargs):
        self.ringPosition = [0,0,0]
        self.wheelOrder = [0,0,0]
        self.rotorPosition = [0,0,0]
        self.plugboard = {n:n for n in range(25)}
        self.ukw = 0
        for key, value in kwargs.items(): #do this with dictionary later
            if key == "ringposition":
                self.ringPosition = ringSettings(value)
            elif key == "wheelorder":
                self.wheelOrder = rotorOrderSettings(value)
            elif key == "rotorposition":
                self.rotorPosition = rotorPositionSettings(value)
            elif key == "plugboard":
                self.plugboard = plugboardSettings(value)
            elif key in {"ukwc","ukw","reflector"}:
                self.ukw = UKW(value,self.wheelOrder) #assumes wheel order exists beforehand
            else:
                print("unknown argument passed to machine initialization")
    
    def encryptLetter(self,letter):
        return str(simulateNumber(ord(letter.upper())-65,self.wheelOrder,self.rotorPosition,self.ringPosition,self.plugboard,self.ukw))

    def encryptLetterVisible(self,letter): #need to make a simulator that returns the internal state at each point, allowing visualization
        pass

    def encryptText(self,text):
        sequence = [ord(t.upper())-65 for t in text]
        cSequence = simulateFull(sequence,self.wheelOrder,self.rotorPosition,self.ringPosition,self.plugboard,self.ukw)
        return "".join([chr(x+65) for x in cSequence])




    
