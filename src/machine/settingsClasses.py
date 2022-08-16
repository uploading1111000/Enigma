import json
class availableSettings:
    #defaults to Enigma I specification
    rotorDefault = [
    ("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q"), 
    ("AJDKSIRUXBLHWTMCQGZNPYFVOE","E"), 
    ("BDFHJLCPRTXVZNYEIWGAKMUSQO","V"),
    ("ESOVPZJAYQUIRHXLNFTGKDCMWB","J"),
    ("VZBRGITYUPSDNHLXAWMJQOFECK","Z")  
    ]
    reflectorDefaults = [
        "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "FVPJIAOYEDRZXWGCTKUQSBNMHL"
        ] 
    defaultNumRotors = 3
    def __init__(self, **kwargs):
        self.rotors = availableSettings.rotorDefault
        self.reflectors = availableSettings.reflectorDefaults
        self.numRotors = availableSettings.defaultNumRotors
        if "filename" in kwargs.keys():
            self.getFromFile(kwargs["filename"])
        self.setFromArguments(**kwargs)
    
    def getFromFile(self, filename):
        pass

    def writeToFile(self, filename):
        writeable = {
            "rotors": self.rotors,
            "reflectors": self.reflectors,
            "number": self.numRotors
        }
        with open(filename,"w") as f:
            json.dump(writeable,f)

    def setFromArguments(self, **kwargs):
        pass

    def generateInternals(self):
        pass

class settings:
    def __init__(self, template: availableSettings,*args):
        pass