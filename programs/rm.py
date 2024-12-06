import os
import shutil
from tools import sanitizeFilename, ensureUnixPath

def executeRm(args, currentPath):
    for name in args:
        targetPath = ensureUnixPath(os.path.join(currentPath, sanitizeFilename(name)))
        if os.path.isdir(targetPath):
            shutil.rmtree(targetPath)
        elif os.path.isfile(targetPath):
            os.remove(targetPath)
        else:
            print(f"err: no such file or directory: {name}")
