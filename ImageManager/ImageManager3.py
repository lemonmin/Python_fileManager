# coding=utf-8

from PIL import Image
import os
import imghdr

basePath = "/Volumes/HD-PNTU3/폰백업/20170418/"
#comparePath = "/Volumes/HD-PNTU3/폰백업/20160823/"
isImages = ["rgb", "gif", "pbm", "pgm", "ppm", "tiff", "rast", "xbm", "jpeg", "bmp", "png", "webp", "exr"]

imageDirectory = []
selectedImages = []


# ---------------------------- METHOD ----------------------------#
def loadImages(path, imageDirectory):
    for f in os.listdir(path):

        if not f.startswith('.'):
            fullPath = os.path.join(path, f)
            if os.path.isfile(fullPath):
                if imghdr.what(fullPath) in isImages:
                    imageDirectory.append(fullPath)
                #else:
                    #print(fullPath,"is not Image!")
            if os.path.isdir(fullPath):
                loadImages(fullPath, imageDirectory)

def openImage(path):
    try:
        requiredImage = Image.open(path)
        return requiredImage
    except IOError:
        print("can't open",path)
        return None

def removeImages():
    global selectedImages
    for i in range (len(selectedImages)):
        print("remove",selectedImages[i])
        #os.unlink(selectedImages[i])
        del selectedImages[i]

def compareImagesToDelete(imageDirectory, selectedImages) :
    baseImage = None
    indexOfBaseKey = 0
    indexOfTargetKey = 0

    while True:
        baseP = imageDirectory[indexOfBaseKey]
        compareP = imageDirectory[indexOfTargetKey]

        if baseImage == None:
            baseImage = openImage(baseP)
            if baseImage == None:
                del imageDirectory[indexOfBaseKey]
                continue
        targetImage = openImage(compareP)
        if targetImage == None :
            del imageDirectory[indexOfTargetKey]
            continue

        if (baseP != compareP) and (baseImage == targetImage):
            selectedImages.append(compareP)
            del imageDirectory[indexOfTargetKey]
        else:
            indexOfTargetKey += 1

        if indexOfTargetKey >= len(imageDirectory):
            indexOfTargetKey = 0
            indexOfBaseKey += 1
        if indexOfBaseKey >= len(imageDirectory):
            print("finish.")
            break

# ------------------------------------------------------------------#

loadImages(basePath, imageDirectory)
#loadImages(comparePath, imageDirectory)
print("count of imageDirectory",len(imageDirectory))
compareImagesToDelete(imageDirectory,selectedImages)
print ("selected Image : ",selectedImages)
removeImages()
print("selected Image : ",selectedImages)
