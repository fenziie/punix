import os
from tools import sanitizeFilename, ensureUnixPath

def executeCat(args, currentPath):
    if len(args) == 2:
        name = args[1]
        targetPath = ensureUnixPath(os.path.join(currentPath, sanitizeFilename(name)))
        if os.path.isfile(targetPath):
            with open(targetPath, 'r') as file:
                print(file.read())
        else:
            print(f"err: no such file: {name}")
    else:
        print("err: expected 1 argument, got: " + str(len(args)-1))
