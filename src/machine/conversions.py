#standardizes inputs
"""
ring position rules:
integers are assumed to be internals
numbers in chars are assumed to be standard numbers, so minus 1 and reverse
letters are assumed to be letter settings, so convert to A=0 and reverse
"""


def ringSettings(settings):
    if isinstance(settings[0],int):
        return settings
    elif isinstance(settings,str):
        return [int(x)-1 for x in settings.split()][::-1]
    else:
        try:
            return [int(x) - 1 for x in settings][::-1]
        except ValueError:
            return [ord(x)-65 for x in settings][::-1]
"""
rotor order rules:
integers are assumed to be internal
letters assumed to be roman numerals (or beta, gamma), so convert and reverse
"""
def rotorOrderSettings(settings):
    NUMERALS = {"I":0,"II":1,"III":2,"IV":3,"V":4,"VI":5,"VII":6,"VIII":7, "BETA":0, "GAMMA":1}
    if isinstance(settings[0], int):
        return settings
    if isinstance(settings, str):
        return [NUMERALS[t.upper()] for t in settings.split()][::-1]
    else:
        return [NUMERALS[t.upper()] for t in settings][::-1]
"""
rotor postion rules:
integers are assumed to be internal
list of letters and strings of letters both used - must be reversed
"""
def rotorPositionSettings(settings):
    if isinstance(settings[0],int):
        return settings
    else:
        return [ord(x)-65 for x in settings][::-1]
"""
plugboard rules:
lists are assumed to be format of (A,B), "AB", [A,B] (anything with a [0] and [1])
whitespace in strings ignored, but must be ordered and paired so "ABCDEFGH" and "AB CD EF GH" are allowed and work the same 
but "Z AB CD EF GH I" will map Z:A. even newlines work if you figure out how to get them in somehow
"""
def plugboardSettings(settings):
    plugs = {n:n for n in range(26)}
    if isinstance(settings,list):
        for pair in settings:
            a = ord(pair[0].upper())-65
            b = ord(pair[1].upper())-65
            plugs[a] = b
            plugs[b] = a
    elif isinstance(settings,str):
        whitespaceless = "".join(settings.split())
        for n in range(0,len(whitespaceless),2):
            a = ord(whitespaceless[n].upper())-65
            b = ord(whitespaceless[n+1].upper())-65
            plugs[a] = b
            plugs[b] = a
    else:
        plugs = settings #internal dictionary
    return plugs
#allows less clutter elsewhere, and manual selection of the UKW TODO: handle specifying somehow
def UKW(UKWC,rotorOrder):
    return UKWC + 2 * (len(rotorOrder) == 4)
