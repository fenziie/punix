import os

def executeLs(currentPath):
    for item in os.listdir(currentPath):
        if os.path.isdir(os.path.join(currentPath, item)):
            print(f"{item}/")
        else:
            print(item)
