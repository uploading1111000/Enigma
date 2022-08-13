from pathlib import Path
import zipfile
def unzip(path):
    result = list(Path(path).rglob("*.[zZ][iI][pP]"))
    for p in result:
        with zipfile.ZipFile(p, "r") as zip_ref:
            zip_ref.extractall(path)
