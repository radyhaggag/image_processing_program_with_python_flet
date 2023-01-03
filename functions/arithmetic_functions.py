import cv2 as cv
from functions.save_image_function import updateTheProcessedImage

from utils.project_enums import ArithmeticOperations
from utils.project_globals import ProjectGlobals


class ArithmeticFunctions():
    def addition(self):
        image1 = cv.imread(ProjectGlobals.FirstSelectedImage)
        image2 = cv.imread(ProjectGlobals.SecondSelectedImage)
        h1, w1 = image1.shape[:2]
        h2, w2 = image2.shape[:2]
        if(h1 != h2 and w1 != w2) :
            image1 = cv.resize(image1, (300, 300))
            image2 = cv.resize(image2 , (300 , 300))
        weightedSum = cv.addWeighted(image1, 0.5, image2, 0.4, 0)
        cv.imshow('Image after addition', weightedSum)
        updateTheProcessedImage(weightedSum)
        cv.waitKey(0)

    def subtraction(self):
        image1 = cv.imread(ProjectGlobals.FirstSelectedImage)
        image2 = cv.imread(ProjectGlobals.SecondSelectedImage)
        sub = cv.subtract(image1, image2)
        cv.imshow('Image after subtraction', sub)
        updateTheProcessedImage(sub)
        cv.waitKey(0)

    def bitwiseAnd(self):
        img1 = cv.imread(ProjectGlobals.FirstSelectedImage)
        img2 = cv.imread(ProjectGlobals.SecondSelectedImage)
        dest_and = cv.bitwise_and(img2, img1, mask=None)
        cv.imshow('Image after bitwiseAnd', dest_and)
        updateTheProcessedImage(dest_and)
        cv.waitKey(0)

    def bitwiseOr(self):
        img1 = cv.imread(ProjectGlobals.FirstSelectedImage)
        img2 = cv.imread(ProjectGlobals.SecondSelectedImage)
        dest_or = cv.bitwise_or(img2, img1, mask=None)
        cv.imshow('Image after bitwiseOr', dest_or)
        updateTheProcessedImage(dest_or)
        cv.waitKey(0)

    def bitwiseXor(self):
        img1 = cv.imread(ProjectGlobals.FirstSelectedImage)
        img2 = cv.imread(ProjectGlobals.SecondSelectedImage)
        dest_xor = cv.bitwise_xor(img2, img1, mask=None)
        cv.imshow('Image after bitwiseXor', dest_xor)
        updateTheProcessedImage(dest_xor)
        cv.waitKey(0)

    def bitwiseNot(self):
        img1 = cv.imread(ProjectGlobals.FirstSelectedImage)
        img2 = cv.imread(ProjectGlobals.SecondSelectedImage)
        dest_not1 = cv.bitwise_not(img1, mask=None)
        dest_not2 = cv.bitwise_not(img2, mask=None)
        cv.imshow('Image after bitwiseNot 1', dest_not1)
        cv.imshow('Image after bitwiseNot 2', dest_not2)
        updateTheProcessedImage(dest_not2)
        cv.waitKey(0)


class ArithmeticFactory():
    global arithmeticFunctions
    arithmeticFunctions = ArithmeticFunctions()

    @staticmethod
    def startProcessing(operation):
        if (operation == ArithmeticOperations.addition.value):
            arithmeticFunctions.addition()
        if (operation == ArithmeticOperations.subtraction.value):
            arithmeticFunctions.subtraction()
        if (operation == ArithmeticOperations.bitwiseAnd.value):
            arithmeticFunctions.bitwiseAnd()
        if (operation == ArithmeticOperations.bitwiseOr.value):
            arithmeticFunctions.bitwiseOr()
        if (operation == ArithmeticOperations.bitwiseXor.value):
            arithmeticFunctions.bitwiseXor()
        if (operation == ArithmeticOperations.bitwiseNot.value):
            arithmeticFunctions.bitwiseNot()
