import cv2 as cv
from functions.save_image_function import updateTheProcessedImage
from utils.project_globals import ProjectGlobals

class ThresholdFunction:
    def threshold(T):
        # Load the image and convert it to grayscale
        image = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        # Threshold the image to create a binary image
        threshold, binary_image = cv.threshold(image, T, 255, cv.THRESH_BINARY)
        # show the image
        cv.imshow('Image After Threshold', binary_image)
        updateTheProcessedImage(binary_image)
        cv.waitKey(0)