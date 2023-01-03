import cv2 as cv
from functions.save_image_function import updateTheProcessedImage
from utils.project_globals import ProjectGlobals

class ResizeImageFunction:
    def resize(width, height):
        # Load the image
        image = cv.imread(ProjectGlobals.FirstSelectedImage)
        # Threshold the image to create a binary image
        resized_image = cv.resize(image, (width, height))
        # show the image
        cv.imshow('Image After Resize', resized_image)
        updateTheProcessedImage(resized_image)
        cv.waitKey(0)