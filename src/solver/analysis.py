from pathlib import Path
import zipfile
import re
from os import walk, remove

#unzips all zip files to the path
def unzip(path):
    result = list(Path(path).rglob("*.[zZ][iI][pP]"))
    for p in result:
        with zipfile.ZipFile(p, "r") as zip_ref:
            zip_ref.extractall(path)

#removes all duplicate texts
def cull(path, max=True):
    filenames = next(walk(path), (None, None, []))[2]
    files = {}
    for x in filenames:
        if x[:5] in files.keys():
            files[x[:5]].append(x)
        else:
            files[x[:5]] = [x]
    for text in files.values():
        text.sort(reverse=max)
        text.pop()
        for file in text:
            remove(path+"/"+file)

#removes prefaces
def depreface(path, line):
    l = re.compile(line)
    filenames = next(walk(path), (None, None, []))[2]
    for x in filenames:
        e = "latin-1"
        try:
            if x[6] == "0":
                e = "utf-8"
        except IndexError:
            pass
        with open(path + "/" + x,"r", encoding=e) as f:
            t = f.readline()
            while t:
                if l.match(t):
                    c = f.readlines()
                    with open(path + "/deprefaced/" + x[:5] + ".txt", "w", encoding=e) as g:
                        g.writelines(c)
                    break 
                t = f.readline()
            else:
                print("Line not found in " + x)

def makeEngimable(path):
    dots = re.compile(r"\.")
    noLetters = re.compile(r"[^a-z^A-Z]")
    filenames = next(walk(path), (None, None, []))[2]
    for x in filenames:
        with open(path + "/" + x,"r", encoding="latin-1") as f:
            t = f.read()
            t = dots.sub("X",t)
            t = noLetters.sub("",t)
            t = t.upper()
        with open(path + "/enigmable/" + x,"w") as f:
            f.write(t)