import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from programs import *
from tools import splitCommand, readInfoFile, writeInfoFile, validateText, sanitizeFilename, ensureUnixPath



def main():
    filesystemPath = "filesystem"
    infoPath = os.path.join(filesystemPath, ".info")
    currentPath = ensureUnixPath(os.path.abspath(filesystemPath))

    if not os.path.exists(filesystemPath):
        os.makedirs(filesystemPath)

    if os.path.exists(infoPath):
        info = readInfoFile(infoPath)
        username = info.get("username", "user")
        hostname = info.get("hostname", "host")
    else:
        print("Welcome to Punix! Please enter the following information.\n")
        while True:
            username = input("Username: ")
            if validateText(username):
                break
            else:
                print("Please make your username between 3 and 15 characters, with only alphanumeric characters, dashes, or underscores.")

        while True:
            hostname = input("Hostname: ")
            if validateText(hostname):
                break
            else:
                print("Please make your hostname between 3 and 15 characters, with only alphanumeric characters, dashes, or underscores.")

        writeInfoFile(infoPath, username, hostname)

    while True:
        command = input(f"{username}@{hostname} $ ")
        args = splitCommand(command)
        if not args:
            continue
        if args[0] in ["help", "?"]:
            executeHelp()
        elif args[0] == "echo":
            executeEcho(args)
        elif args[0] == "clear":
            clearScreen()
        elif args[0] == "touch":
            executeTouch(args[1:], currentPath)
        elif args[0] == "cd":
            currentPath = executeCd(args, currentPath)
        elif args[0] == "mkdir":
            executeMkdir(args[1:], currentPath)
        elif args[0] == "pwd":
            executePwd(currentPath)
        elif args[0] == "ls":
            executeLs(currentPath)
        elif args[0] == "rm":
            executeRm(args[1:], currentPath)
        elif args[0] == "cat":
            executeCat(args, currentPath)
        elif args[0] == "eval":
            executeEval(args)
        elif args[0] == "edit":
            executeEdit(args)
        elif args[0] == "neofetch":
            executeNeofetch(username, hostname)
        elif args[0] == "exit":
            break
        else:
            print("err: command invalid")

if __name__ == "__main__":
    main()
