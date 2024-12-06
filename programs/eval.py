import re

def isValidMathExpression(expression):
    pattern = re.compile(r'^-?\d+(\.\d+)?([\s\+\-\*\/\.\d]+)*$')
    return pattern.match(expression) is not None

def executeEval(args):
    if len(args) > 1:
        expression = ' '.join(args[1:])
        if isValidMathExpression(expression):
            try:
                result = eval(expression)
                print(result)
            except Exception as e:
                print(f"err: {e}")
        else:
            print("err: invalid mathematical expression")
    else:
        print("err: expected 1 argument, got: " + str(len(args)-1))
