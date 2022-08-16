import json
class availableSettings:
    #defaults to Enigma I specification
    rotorDefault = [
    ("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q", 0), 
    ("AJDKSIRUXBLHWTMCQGZNPYFVOE","E", 0), 
    ("BDFHJLCPRTXVZNYEIWGAKMUSQO","V", 0),
    ("ESOVPZJAYQUIRHXLNFTGKDCMWB","J", 0),
    ("VZBRGITYUPSDNHLXAWMJQOFECK","Z", 0)  
    ]
    reflectorDefaults = [
        "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "FVPJIAOYEDRZXWGCTKUQSBNMHL"
        ] 
    allowedDefault = [0,0,0] #defines which rotors can go where and doubles as specifying how many rotors there are
    def __init__(self, **kwargs):
        self.rotors = self.rotorDefault
        self.reflectors = self.reflectorDefaults
        self.allowed = self.allowedDefault
        self.num = len(self.allowedDefault)
        if "filename" in kwargs.keys():
            self.getFromFile(kwargs["filename"])
        self.setFromArguments(**kwargs)
    
    def getFromFile(self, filename):
        #needs sanitation
        with open(filename,"r") as f:
            dict = json.load(f)
        try:
            self.rotors = dict["rotors"]
            self.reflectors = dict["reflectors"]
            self.numRotors = dict["allowed"]
        except KeyError:
            print("Invalid file! Maybe json formatting wrong or missing a specification")
        if self.rotors == "default":
            self.rotors = self.rotors
        if self.reflectors == "default":
            self.reflectors = self.reflectorDefaults
        if self.allowed == "default":
            self.allowed = self.allowedDefault
            self.num = len(self.allowedDefault)
 
    def writeToFile(self, filename):
        writeable = {
            "rotors": self.rotors,
            "reflectors": self.reflectors,
            "allowed": self.allowed
        }
        with open(filename,"w") as f:
            json.dump(writeable,f)

    def setFromArguments(self, **kwargs):
        for kwarg,value in kwargs.items():
            if kwarg == "rotors":
                self.rotors = value
            elif kwarg == "reflectors":
                self.reflectors = value
            elif kwarg == "allowed":
                self.allowed = value
                self.num = len(value)

    def generateInternals(self):
        pass

class settings:
    def __init__(self, template: availableSettings,*args):
        pass