import cv2 as cv
import matplotlib.pyplot as plt
from functions.save_image_function import updateTheProcessedImage

from utils.project_enums import HistogramOperations
from utils.project_globals import ProjectGlobals


class HistogramFunctions():
    def calcHistogram(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        histogram = cv.calcHist(
            images=[img],
            channels=[0],
            mask=None,
            histSize=[256],
            ranges=[0, 256],
        )
        plt.plot(histogram)
        plt.show()

    def histogramEqualization(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        imageAfterHistogramEqualization = cv.equalizeHist(img)
        cv.imshow("Histogram Equalization", imageAfterHistogramEqualization)
        updateTheProcessedImage(imageAfterHistogramEqualization)
        cv.waitKey()
        cv.destroyAllWindows()


class HistogramFactory():
    global histogramFunctions
    histogramFunctions = HistogramFunctions()

    @staticmethod
    def startProcessing(operation):
        if (operation == HistogramOperations.histogramCalculation.value):
            histogramFunctions.calcHistogram()
        if (operation == HistogramOperations.histogramEqualization.value):
            histogramFunctions.histogramEqualization()
