import os
from tools import ensureUnixPath

def executePwd(currentPath):
    relativePath = os.path.relpath(currentPath, "filesystem")
    if relativePath == ".":
        print("/")
    else:
        print(f"/{ensureUnixPath(relativePath)}")
