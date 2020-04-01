import codecs
def readPlates(clientCar):

    path = 'C:\\Users\\Shon\\Desktop\\Python Programs\\LicenceplateR\\dataBase\\Licenceplates.txt'
    plateList = []

    with codecs.open(path, 'r', "utf-8") as f:
        for plates in f:
            #print(names)
            plateList.append(plates.strip())

    print(plateList)
    for c in plateList:
        if c == clientCar:
            return True