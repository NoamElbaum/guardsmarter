import codecs

def readNames(clientName):

    path = 'C:\\Users\\Shon\\Desktop\\Python Programs\\LicenceplateR\\dataBase\\Names.txt'
    nameList = []

    with codecs.open(path, 'r', "utf-8") as f:
        for names in f:
            #print(names)
            nameList.append(names.strip())

    #print(nameList)
    for c in nameList:
        if c == clientName:
            return True