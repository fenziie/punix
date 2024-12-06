import re, os

def clearScreen():
    os.system("clear")

def validateText(text):
    return bool(re.match("^[a-zA-Z0-9_-]{3,15}$", text))

def splitCommand(command):
    return command.split() if command.strip() else []

def readInfoFile(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            info = {}
            for line in lines:
                if ' = ' in line:
                    key, value = line.strip().split(' = ', 1)
                    info[key] = value
            return info
    except Exception as e:
        print(f"Error: {e}")
        return {}

def writeInfoFile(filepath, username, hostname):
    try:
        with open(filepath, 'w') as file:
            file.write(f"username = {username}\n")
            file.write(f"hostname = {hostname}\n")
    except Exception as e:
        print(f"Error: {e}")

def sanitizeFilename(filename):
    return re.sub(r'[\\/:*?"<>|]', "", filename)

def ensureUnixPath(path):
    return path.replace("\\", "/")

