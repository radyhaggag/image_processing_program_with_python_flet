import cv2 as cv

from functions.save_image_function import updateTheProcessedImage
from utils.project_enums import ImageConversionOperations
from utils.project_globals import ProjectGlobals


class ImageConversionFunctions:
    def imageToGrayScale(self):
        image = cv.imread(ProjectGlobals.FirstSelectedImage)
        # we can also on imread assign 0 to the flag to convert the image to gray scale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        cv.imshow('Gray scale image', gray)
        updateTheProcessedImage(gray)
        cv.waitKey(0)

    def imageToBinary(self):
        image = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        # Threshold the image to create a binary image
        threshold, binary_image = cv.threshold(
            image, 127, 255, cv.THRESH_BINARY)
        cv.imshow('Binary image', binary_image)
        updateTheProcessedImage(binary_image)
        cv.waitKey(0)

    def imageToRGB(self):
        image = cv.imread(ProjectGlobals.FirstSelectedImage)
        rgbImage = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        cv.imshow('RGB image', rgbImage)
        updateTheProcessedImage(rgbImage)
        cv.waitKey(0)


class ImageConversionFactory:
    global imageConversionFunctions
    imageConversionFunctions = ImageConversionFunctions()

    @staticmethod
    def startProcessing(operation):
        if (operation == ImageConversionOperations.imageToGrayScale.value):
            imageConversionFunctions.imageToGrayScale()
        if (operation == ImageConversionOperations.imageToBinary.value):
            imageConversionFunctions.imageToBinary()
        if (operation == ImageConversionOperations.imageToRGB.value):
            imageConversionFunctions.imageToRGB()
