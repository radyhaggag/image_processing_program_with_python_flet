import cv2 as cv
import numpy as np
from functions.save_image_function import updateTheProcessedImage
from utils.project_enums import SpatialDomainOperations

from utils.project_globals import ProjectGlobals


class SpatialDomainFunctions():
    # 1 COLOR IMG  0 GRAY  -1 UNCHANGED
    def identityTransformation(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        img = img*1
        cv.imshow("Identity Transformation image", img)
        updateTheProcessedImage(img)
        cv.waitKey()
        cv.destroyAllWindows()

    def negativeTransformation(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        h, w = img.shape
        for row in range(h):
            for col in range(w):
                img[row][col] = 255-img[row][col]
        cv.imshow("Negative Transformation image", img)
        updateTheProcessedImage(img)
        cv.waitKey()
        cv.destroyAllWindows()

    def logTransformation(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        h, w = img.shape
        # assume c equal 20
        for row in range(h):
            for col in range(w):
                img[row][col] = int(20*(np.log2(1+img[row][col])))
        cv.imshow("Log Transformation image", img)
        updateTheProcessedImage(img)
        cv.waitKey()
        cv.destroyAllWindows()

    def powerLawTransformation(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        h, w = img.shape
        for row in range(h):
            for col in range(w):
                img[row][col] = 255*(img[row][col]/255)**0.5
        cv.imshow("Power Law Transformation image", img)
        updateTheProcessedImage(img)
        cv.waitKey()
        cv.destroyAllWindows()

    def contrastStretching(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        h, w = img.shape
        a = np.min(img)
        b = np.max(img)
        R = b-a
        for row in range(h):
            for col in range(w):
                img[row][col] = ((img[row][col]-a)/R)*255
                img[row][col] = np.rint(img[row][col])
        cv.imshow("Contrast Stretching", img)
        updateTheProcessedImage(img)
        cv.waitKey()
        cv.destroyAllWindows()

    def intensitySlicing(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        h, w = img.shape
        img1 = np.zeros((h, w), dtype='uint8')
        # Specify the min and max range
        min_range = 10  # A
        max_range = 60  # B
        # Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
        for i in range(h):
            for j in range(w):
                if img[i, j] > min_range and img[i, j] < max_range:
                    img1[i, j] = 255
                else:
                    img1[i, j] = 0
        # Display the image
        cv.imshow('Intensity Slicing image', img1)
        updateTheProcessedImage(img)
        cv.waitKey(0)


class TransformationFactory():
    global transformationFunctions
    transformationFunctions = SpatialDomainFunctions()

    @staticmethod
    def startProcessing(operation):
        if (operation == SpatialDomainOperations.contrastStretching.value):
            transformationFunctions.contrastStretching()
        if (operation == SpatialDomainOperations.identityTransformation.value):
            transformationFunctions.identityTransformation()
        if (operation == SpatialDomainOperations.intensitySlicing.value):
            transformationFunctions.intensitySlicing()
        if (operation == SpatialDomainOperations.logTransformation.value):
            transformationFunctions.logTransformation()
        if (operation == SpatialDomainOperations.negativeTransformation.value):
            transformationFunctions.negativeTransformation()
        if (operation == SpatialDomainOperations.powerLawTransformation.value):
            transformationFunctions.powerLawTransformation()
