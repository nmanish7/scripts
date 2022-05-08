import hashlib
from pathlib import Path
from tqdm import tqdm


USERINPUTFILENAME = "/usr/share/wordlists/rockyou.txt"  # Give the Input File
FILENAME = Path(USERINPUTFILENAME) if Path(
    USERINPUTFILENAME).exists() else None
if not FILENAME:
    print(f"{USERINPUTFILENAME} is not exist.")
    exit()

ENCODING = "latin-1"  # Give the Encoding


def file_next_line(filename: str, encoding: str):

    with open(file=filename, encoding=encoding) as file:

        for inner_line in file:
            yield bytes(inner_line.replace("\n", ""), encoding)


file_object = file_next_line(FILENAME, ENCODING)


FILENAMEOUT = f"{FILENAME.name.rsplit('.', maxsplit=1)[0]}_sha1Hash.txt"
ENCODINGOUT = "utf-8"

with open(file=FILENAMEOUT, mode="w", encoding=ENCODINGOUT) as file_write:

    for line in tqdm(file_object):
        hash_obj = hashlib.sha1(line)
        SHA1HASH = hash_obj.hexdigest()
        file_write.write(f"{SHA1HASH}\n")
