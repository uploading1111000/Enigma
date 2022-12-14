import json

def indexCoincidence(text):
    frequencies = [0 for x in range(26)]
    for x in text:
        frequencies[x] += 1
    sum = 0
    for i in frequencies:
        sum += i * (i - 1)
    n = len(text)
    return sum / (n * (n+1))
    
def getNGrams(text,n):
    return [text[i:i+n] for i in range(len(text)-n + 1)]

def generateAllNGrams(n): #recursively finds all the possible ngrams of length n by calling recursive
    if n == 1:
        return [chr(x) for x in range(65,91)]
    else:
        lower = generateAllNGrams(n-1)
        return [chr(x) + t for t in lower for x in range(65,91)]

def countNGrams(text,n,scores):
    for i in range(len(text)-n+1):
        scores[text[i:i+n]] += 1

def getscores(file):
    with open(file,"r") as f:
        return json.load(f)

"""print("generating ngram dictionaries")
oneGram = generateAllNGrams(3)
twoGram = generateAllNGrams(3)              #not in use
threeGram = generateAllNGrams(3)
#fourGram = generateAllNGrams(4)"""

print("importing ngram frequencies")
frequencies = [
    getscores("src/solver/final1gram.json"),
    getscores("src/solver/final2gram.json"),
    getscores("src/solver/final3gram.json"),
    #getscores("src/solver/final4gram.json")
]

def nGramScore(text,n):
    letters = "".join([chr(x+65) for x in text]) #makes it possible to read numbers directly from internal
    grams = getNGrams(letters,n)
    score = 0
    for gram in grams:
        score += (frequencies[n-1])[gram]
    return score
