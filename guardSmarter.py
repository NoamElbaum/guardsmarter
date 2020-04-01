
import speech_recognition as sr
import codecs
from PIL import Image
import pytesseract as ocr
import numpy as np
import cv2



def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hello, please say your name :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,  language='he')
            return text
        except:
            print("Sorry could not recognize what you said")
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
def rec(userPlate):

    imageName = userPlate ##image name

    plateNum = []
    citizenPlate = ['5', '5', '6', '0', '4', '2', '0', '1']
    img = Image.open(imageName)
    thresh = 70
    fn = lambda x: 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')

    width, height = r.size

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    image = cv2.imread(imageName)
    imageClean = cv2.imread(imageName)
    original = image.copy()

    ##cv2 recognition
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([10, 120, 120], dtype="uint8")
    upper = np.array([25, 255, 255], dtype="uint8")
    mask = cv2.inRange(image, lower, upper)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    bigW = 0
    bigH = 0
    bigX = 0
    bigY = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if bigW * bigH <= w*h:
            bigW = w
            bigH = h
            bigX = x
            bigY = y


        cv2.rectangle(original, (x, y), (x + w, y + h), (36,255,12), 2)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    #croping-cv2
    cv2.rectangle(original, (bigX, bigY), (bigX+bigW, bigY+bigH), (255,0,0), 2)
    crop_img = imageClean[bigY:bigY+bigH, bigX:bigX+bigW] ##for debug
    crop_img_mask = mask[bigY:bigY+bigH, bigX:bigX+bigW]

    ##gray image cropped
    grayImage = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)


    ##tesseract
    plate = ocr.image_to_string(crop_img_mask)
    plate1 = ocr.image_to_string(crop_img)
    plate2 = ocr.image_to_string(grayImage)
    plate3 = ocr.image_to_string(blackAndWhiteImage)
    print("regular crop is : " + plate1)
    print("mask crop is : " + plate)
    print("gray crop is : " + plate2)
    print("gray(black white) crop is : " + plate3)


    for i in plate:
        if i.isdigit():
            plateNum.append(i)
    print(plateNum)
    return ''.join(plateNum)

    ##debug image cv2
    cv2.imshow('mask', mask)
    cv2.imshow('original', original)
    cv2.imshow("Cropped cv2", crop_img)
    cv2.imshow("Cropped cv2 masked", crop_img_mask)
    cv2.imshow("Cropped cv2 gray(black white)", blackAndWhiteImage)
    cv2.waitKey()