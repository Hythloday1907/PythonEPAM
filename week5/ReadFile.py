def readFile(file):

    myObject = {}
    with open(file) as f:
            forline in f.readlines():
                key, value = line.rstrip("\n").split("=")
                print(key, "-->", value)
            if(not key in myObject):
                myObject[key] = value
            else:
                print("Duplicated assignment of key '%s'" % key)