
def loadCreds(cred):
    myCreds = {}
    with open("config.txt") as f:
        for line in f.readlines():
            key, value = line.rstrip("\n").split("=")
            myCreds[key] = value

    return myCreds[cred]