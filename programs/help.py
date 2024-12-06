helpText = """Commands:
help / ?       show this menu
exit           exit Punix
clear          clear screen
echo x         print x to stdout
touch x        create an empty file x
cd x           change directory to x
mkdir x        create a directory x
pwd            print working directory
ls             list directory contents
rm x           remove file or directory x
cat x          display contents of file x
eval x         evaluate python-style maths equation x
neofetch       displays (fake) system information
edit x         edit a file (x) using a line-by-line text editor"""

def executeHelp():
    print(helpText)
