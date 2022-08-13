from machine.constants import rotors, reverseRotors, reflectors, notches, fourRotors, reverseFourRotors
from machine.conversions import *
#wheels are back to front, so wheel index 0 is the rightmost
def simulateNumber(number,wheelorder=[0,1,2],rotorposition=[0,0,0],ringposition=[0,0,0], plugboard={n:n for n in range(26)}, UKW=0):
    p1 = plugboard[number]
    p2 = rotorpass(p1,wheelorder,rotorposition,ringposition,UKW)
    p3 = plugboard[p2]
    return p3

def simulateFull(sequence,wheelorder=[0,1,2],rotorposition=[0,0,0],ringposition=[0,0,0], plugboard={n:n for n in range(26)}, UKW=0):
    final = []
    for Pletter in sequence:
        final.append(simulateNumber(Pletter,wheelorder,rotorposition,ringposition,plugboard,UKW))
    return final

def rotorpass(letter,wheelorder,rotorposition,ringposition,UKW):
    turnrotors(wheelorder,rotorposition) #rotors actually turn before key is pressed
    l0 = letter #forward
    l1 = ((rotors[wheelorder[0]])[(l0+rotorposition[0]-ringposition[0]) % 26]-rotorposition[0]+ringposition[0]) % 26
    l2 = ((rotors[wheelorder[1]])[(l1+rotorposition[1]-ringposition[1]) % 26]-rotorposition[1]+ringposition[1]) % 26
    l3 = ((rotors[wheelorder[2]])[(l2+rotorposition[2]-ringposition[2]) % 26]-rotorposition[2]+ringposition[2]) % 26
    if len(wheelorder)==4:
        l3 = ((fourRotors[wheelorder[3]])[(l3+rotorposition[3]-ringposition[3]) % 26]-rotorposition[3]+ringposition[3]) % 26
    reflect = reflectors[UKW]
    l4 = reflect[l3] #reflect 
    if len(wheelorder)==4:
        l4 = ((reverseFourRotors[wheelorder[3]])[(l4+rotorposition[3]-ringposition[3]) % 26]-rotorposition[3]+ringposition[3]) % 26
    l5 = ((reverseRotors[wheelorder[2]])[(l4+rotorposition[2]-ringposition[2]) % 26]-rotorposition[2]+ringposition[2]) % 26 #backward
    l6 = ((reverseRotors[wheelorder[1]])[(l5+rotorposition[1]-ringposition[1]) % 26]-rotorposition[1]+ringposition[1]) % 26
    l7 = ((reverseRotors[wheelorder[0]])[(l6+rotorposition[0]-ringposition[0]) % 26]-rotorposition[0]+ringposition[0]) % 26
    return l7
def turnrotors(wheelorder,rotorposition):
    #middlewheel done first because of double stepping
    if rotorposition[1] in notches[wheelorder[1]]:
        rotorposition[1] = (rotorposition[1] + 1) % 26
        rotorposition[2] = (rotorposition[2] + 1) % 26
    #then rightmost wheel - this may lead to middle wheel stepping twice often but i believe this shouldn't be possible during normal operation
    if rotorposition[0] in notches[wheelorder[0]]:
        rotorposition[1] = (rotorposition[1] + 1) % 26
    rotorposition[0] = (rotorposition[0] + 1) % 26 #finally a normal step
    #rotor[3] (if it exists) does not step

#rarely used
def simulateWords(word,wheelorder=[0,1,2],rotorposition=[0,0,0],ringposition=[0,0,0], plugboard={n:n for n in range(26)}, UKWC = 0):
    numbers = [ord(x)-65 for x in word]
    c = simulateFull(numbers,wheelorder,rotorposition,ringposition,plugboard,UKWC)
    return "".join([chr(x+65) for x in c])

def simulateStd(word,wheelorder=["I","II","III"],rotorposition="AAA",ringposition=[1,1,1], plugboard={n:n for n in range(26)}, UKWC = 0): 
    """
    Interface that simulates enigma given settings in standard form/mixed standard form
    Internal form is different from the way enigma is typical written as such:
    Internal is right to left, e.g rotorposition[0] is the position of the rightmost rotor when in standard form is the leftmost
    Internal uses entirely numbers and no characters (in standard characters denote almost all settings of the machine (ring settings are sometimes numerical, but 1 off the internal) aswell as the inputs and outputs)
    Standard uses roman numerals for the rotors in use

    Note: this does not do any error handling, just allows more inputs. Make sure to sanitise inputs elsewhere
    Note: will not accept A=0 for ringposition
    """
    NUMERALS = {"I":0,"II":1,"III":2,"IV":3,"V":4,"VI":5,"VII":6,"VIII":7, "BETA":0, "GAMMA":1}
    if isinstance(word[0],str): #for text input
        text=[ord(x)-65 for x in word.replace(" ","").upper()]
    else:
        text = word #for numerical input
    wheels = rotorOrderSettings(wheelorder)
    positions = rotorPositionSettings(rotorposition)
    rings = ringSettings(ringposition)
    plugs = plugboardSettings(plugboard)
    UKW = UKW(UKWC,wheelorder)
    out = simulateFull(text,wheels,positions,rings,plugs,UKW)
    return "".join([chr(t+65) for t in out])

 

