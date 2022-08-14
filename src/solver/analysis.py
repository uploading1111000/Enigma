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
        try:
            if x[6] == "0":
                e = "utf-8"
            elif x[6] == "8":
                e = "latin"
        except IndexError:
            e = "ascii"
        with open(path + "/" + x,"r", encoding=e) as f:
            t = f.readline()
            n = 0
            while t:
                if n < 50:
                    n += 1
                    print(t)
                if l.match(t):
                    v = ""
                    while t:
                        t = f.readline()
                        v = v + t + "\n"
                    with open(path + "/deprefaced/s" + x[:5] + ".txt", "w", encoding=e) as g:
                        g.write(v)
                    break 
                t = f.readline()
            else:
                print("Line not found in " + x)