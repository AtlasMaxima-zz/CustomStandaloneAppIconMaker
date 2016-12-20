import os
import subprocess

z = 16
x = "sips -z "
sipsList = []
intList = []
LoopTwoList = []
intLoopTwo = []
for i in range(6):
    intList.append(str(z))
    intLoopTwo.append(str(z))
    sipsString = x+str(z)+" "+str(z)
    z*=2
    sipsList.append(sipsString)
    LoopTwoList.append(sipsString)
sipsList.remove("sips -z 64 64")
intList.remove("64")
LoopTwoList.append("sips -z 1024 1024")
LoopTwoList.remove("sips -z 16 16")
LoopTwoList.remove("sips -z 128 128")
intLoopTwo.remove("64")

userRelativePath = input("Enter the absolute path: ")
userImage = input("Enter the image name: ")

directoryPath = ''

def makeDirectory():
    userDir = input("Enter the directory name: ")
    print("The directory name you've entered is " + userDir)
    pathName = ''
    print(userDir + " is now undergoing directory creation...")
    print("...")
    print("...")
    print("...")
    try:
        if not os.path.isdir(userDir):
            pathName = "~/Desktop/" + userDir + ".iconset"
            os.makedirs(os.path.expanduser(pathName))
            directoryPath = userDir + ".iconset"
            print("You've successfully made a directory!", directoryPath)
            createIcons(userImage, userRelativePath, directoryPath, sipsList, intList, LoopTwoList, intLoopTwo)
    except IOError as e:
        print("Error", e)
    else:
        print()
        print(directoryPath + " has been successfully created!")
        print("The relative path name is " + pathName)

def createIcons(userImage, userRelativePath, directoryPath, sipsList, intList, LoopTwoList, intLoopTwo):

    try:
        for i in range(5):
            iconOutput = (sipsList[i] + " " + userRelativePath + "/" + userImage + ".png" + " --out " + userRelativePath + "/" + directoryPath + "/icon_" +
                          intList[i] + "x" + intList[i] + ".png")
            output = subprocess.getstatusoutput(iconOutput)
        for j in range(5):
            secondLoop = (LoopTwoList[j] + " " + userRelativePath + "/" + userImage + ".png" + " --out " + userRelativePath + "/" + directoryPath + "/icon_" +
                          intLoopTwo[j] + "x" + intLoopTwo[j] + "@2x.png")
            secondLoopOutput = subprocess.getstatusoutput(secondLoop)
        createIcns = subprocess.getstatusoutput("iconutil -c icns "+userRelativePath+"/"+directoryPath)
    except:
        print("Image Error")

makeDirectory()


