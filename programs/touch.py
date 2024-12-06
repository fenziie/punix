import os
from tools import sanitizeFilename, ensureUnixPath

def executeTouch(args, currentPath):
    for filename in args:
        sanitizedFilename = sanitizeFilename(filename)
        filepath = ensureUnixPath(os.path.join(currentPath, sanitizedFilename))
        if os.path.exists(filepath):
            print(f"err: file or directory named '{sanitizedFilename}' already exists")
        elif os.path.isdir(filepath):
            print(f"err: a directory with the name '{sanitizedFilename}' already exists")
        else:
            open(filepath, 'a').close()
