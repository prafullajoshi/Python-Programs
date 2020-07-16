if __name__ == '__main__':
    print("Hello")

    sent = "This is new sent"
    splitted = sent.split()
    args = splitted[1:]
    print(args)
    print(",".join(args))
    print(splitted)

    N = int(input())
    result = []
    for i in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("result." + cmd)
        else:
            print(result)
