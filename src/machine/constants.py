rotorsString=[
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ", #I    | Used by every enigma
    "AJDKSIRUXBLHWTMCQGZNPYFVOE", #II   | Used by every enigma
    "BDFHJLCPRTXVZNYEIWGAKMUSQO", #III  | Used by every enigma
    "ESOVPZJAYQUIRHXLNFTGKDCMWB", #IV   | Used by every wartime enigma
    "VZBRGITYUPSDNHLXAWMJQOFECK", #V    | Used by every wartime enigma
    "JPGVOUMFYQBENHZRDKASXLICTW", #VI   | Used by navy enigmas
    "NZJHGRCXMYSWBOUFAIVLPEKQDT", #VII  | Used by navy enigmas
    "FKQHTLXOCBJSPDZRAMEWNIUYGV"  #VIII | Used by navy enigmas
]
notches = [
    {ord("Q")-65}, #I
    {ord("E")-65}, #II  
    {ord("V")-65}, #III
    {ord("J")-65}, #IV
    {ord("Z")-65}, #V
    {ord("Z")-65,ord("M")-65}, #VI
    {ord("Z")-65,ord("M")-65}, #VII
    {ord("Z")-65,ord("M")-65}  #VII
]
fourRotorString = [               #4th rotor used by Uboat enigmas - special shape means that only 2 rotor designs used - do not step, making them add little to the analysis
    "LEYJVCNIXWPBQMDRTAKZGFUHOS", #beta
    "FSOKANUERHMBTIYCWLQPZXVGJD"  #gamma
]
reflectorStrings = [
    "YRUHQSLDPXNGOKMIEBFZCWVJAT", #UKWB - in use for majority of war
    "FVPJIAOYEDRZXWGCTKUQSBNMHL", #UKWC - in use at end of war
    "ENKQAUYWJICOPBLMDXZVFTHRGS", #UKWb - used in 4 rotor M4 machine used in U-boats
    "RDOBJNTKVEHMLFCWZAXGYIPSUQ"  #UKWc - used in 4 rotor M4 machine used in U-boats
]
#TODO add more reflector strings for the M4
rotors = []
reverseRotors = []
fourRotors = []
reverseFourRotors = []
for rotor in rotorsString:
    line = []
    reverseLine = [26 for x in range(26)]
    for n, letter in enumerate(rotor):
        line.append(ord(letter)-65)
        reverseLine[ord(letter)-65] = n
    rotors.append(line)
    reverseRotors.append(reverseLine)
for rotor in fourRotorString:
    line = []
    reverseLine = [26 for x in range(26)]
    for n, letter in enumerate(rotor):
        line.append(ord(letter)-65)
        reverseLine[ord(letter)-65] = n
    fourRotors.append(line)
    reverseFourRotors.append(reverseLine)
reflectors = [[ord(x)-65 for x in reflector] for reflector in reflectorStrings]

#IDEA: make the wirings and settings settable by file