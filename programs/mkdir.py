import os
from tools import sanitizeFilename, ensureUnixPath

def executeMkdir(args, currentPath):
    for dirname in args:
        sanitizedDirname = sanitizeFilename(dirname)
        dirpath = ensureUnixPath(os.path.join(currentPath, sanitizedDirname))
        if os.path.exists(dirpath):
            print(f"err: file or directory named '{sanitizedDirname}' already exists")
        elif os.path.isfile(dirpath):
            print(f"err: a file with the name '{sanitizedDirname}' already exists")
        else:
            os.makedirs(dirpath, exist_ok=True)
