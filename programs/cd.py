import os
from tools import ensureUnixPath

def executeCd(args, currentPath):
    if len(args) > 1:
        targetPath = args[1]
        if targetPath.startswith("/"):
            newPath = ensureUnixPath(os.path.abspath(os.path.join("filesystem", targetPath.lstrip("/"))))
        else:
            newPath = ensureUnixPath(os.path.abspath(os.path.join(currentPath, targetPath)))

        filesystemRoot = ensureUnixPath(os.path.abspath("filesystem"))
        if not newPath.startswith(filesystemRoot):
            print("err: cannot navigate out of the filesystem folder")
            return currentPath
        if os.path.isdir(newPath):
            return newPath
        else:
            print("err: no such directory")
    else:
        print("err: missing directory argument")
    return currentPath
