def executeEcho(args):
    if len(args) > 1:
        print(' '.join(args[1:]))
    else:
        print("err: no text provided to echo")
