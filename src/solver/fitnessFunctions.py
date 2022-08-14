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

def generateAllNGrams(n):
    if n == 1:
        return [chr(x) for x in range(65,91)]
    else:
        return [chr(x) + t for t in generateAllNGrams(n-1) for x in range(65,91)]