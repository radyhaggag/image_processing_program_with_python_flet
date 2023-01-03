import cv2 as cv
from functions.save_image_function import updateTheProcessedImage
from utils.project_globals import ProjectGlobals


class ExtractROIFunction:
    def extractROI():
        # Load the image
        image = cv.imread(ProjectGlobals.FirstSelectedImage)
        # Select the region of interest (ROI)
        roi = image[200: 300, 200: 480]
        # show the roi image
        cv.imshow('Image after extract a ROI', roi)
        updateTheProcessedImage(roi)
        cv.waitKey(0)
