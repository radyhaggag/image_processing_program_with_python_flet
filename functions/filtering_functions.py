import cv2 as cv
import matplotlib.pyplot as plt

import numpy as np
from PIL import Image, ImageFilter
from functions.save_image_function import updateTheProcessedImage

from utils.project_enums import FilteringOperations
from utils.project_globals import ProjectGlobals


class FilteringFunctions():
    def averageFiltering(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage)
        # averageBlurImage = cv.blur(img, (5, 5))
        # cv.imshow('After Average Blur', averageBlurImage)
        # updateTheProcessedImage(averageBlurImage)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        imgWithMoreBlurred = np.hstack([img,
                                        cv.blur(img, (3, 3)),
                                        cv.blur(img, (5, 5)),
                                        cv.blur(img, (7, 7)),
                                        cv.blur(img, (13, 13)),
                                        ])
        cv.imshow('Average Filter', imgWithMoreBlurred)
        updateTheProcessedImage(imgWithMoreBlurred)
        cv.waitKey(0)

    def gaussianFiltering(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage)
        # gaussianBlurImage = cv.GaussianBlur(img, (5, 5), 10)
        # cv.imshow('After Gaussian Blur', gaussianBlurImage)
        # updateTheProcessedImage(gaussianBlurImage)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        # apply more than one blur
        imgWithMoreBlurred = np.hstack([img,
                                        cv.GaussianBlur(img, (3, 3), 0),
                                        cv.GaussianBlur(img, (5, 5), 0),
                                        cv.GaussianBlur(img, (7, 7), 0),
                                        cv.GaussianBlur(img, (13, 13), 0),
                                        ])
        cv.imshow('Gaussian Filter', imgWithMoreBlurred)
        updateTheProcessedImage(imgWithMoreBlurred)
        cv.waitKey(0)

    def medianFiltering(self):
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        # medianBlurImage = cv.medianBlur(img, 5)  # remove salt and pepper noise
        # cv.imshow('After', medianBlurImage)
        # updateTheProcessedImage(medianBlurImage)
        # cv.waitKey(0)
        imgWithMoreBlurred = np.hstack([img,
                                        cv.medianBlur(img, 3),
                                        cv.medianBlur(img, 5),
                                        cv.medianBlur(img, 7),
                                        cv.medianBlur(img, 13),
                                        ])
        cv.imshow('Median Filter', imgWithMoreBlurred)
        updateTheProcessedImage(imgWithMoreBlurred)
        cv.waitKey(0)

    def minFiltering(self):
        img = Image.open(ProjectGlobals.FirstSelectedImage)
        # Remove Salt noise
        minFilter = img.filter(ImageFilter.MinFilter(size=3))
        img.show()
        updateTheProcessedImage(minFilter)
        minFilter.show(title='Min Filter Image')

    def maxFiltering(self):
        img = Image.open(ProjectGlobals.FirstSelectedImage)
        # Remove Pepper noise
        maxFilter = img.filter(ImageFilter.MaxFilter(size=3))
        img.show()
        updateTheProcessedImage(maxFilter)
        maxFilter.show(title='Max Filter Image')

    def laplacianFiltering(self):
        # Load the image and Convert the image to grayscale
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        # Create the Laplacian kernel
        kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        # Apply the Laplacian filter to the image
        laplacian = cv.filter2D(img, cv.CV_64F, kernel)
        # show the resulting image
        cv.imshow('Image Before laplacian filter', img)
        cv.imshow('Image after laplacian filter', laplacian)
        updateTheProcessedImage(laplacian)
        cv.waitKey(0)

    def laplacianOfGaussianFiltering(self):
        # Load the image and Convert the image to grayscale
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        # Apply Gaussian Blur
        blur_image_gaussian = cv.GaussianBlur(img, (3, 3), 0)
        # Apply the Laplacian filter to the image
        laplacian = cv.Laplacian(blur_image_gaussian, cv.CV_64F, 3)
        # show the resulting image
        cv.imshow('Image Before LOG filter', img)
        cv.imshow('Image after laplacian filter', laplacian)
        updateTheProcessedImage(laplacian)
        cv.waitKey(0)

    def prewittFiltering(self):
        # Load the image and Convert the image to grayscale
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        # Apply Gaussian Blur
        blur_image_gaussian = cv.GaussianBlur(img, (3, 3), 0)
        # Create the Prewitt kernels
        kernelX = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        kernelY = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        # Apply the Prewitt operator to the image
        prewittX = cv.filter2D(blur_image_gaussian, -1, kernelX)
        prewittY = cv.filter2D(blur_image_gaussian, -1, kernelY)
        # Combine the gradient magnitudes along the two axes
        prewitt = prewittX + prewittY
        # show the resulting image
        # cv.imshow('PrewittX', prewittX)
        # cv.imshow('PrewittY', prewittY)
        cv.imshow('After prewitt filter', prewitt)
        updateTheProcessedImage(prewitt)
        cv.waitKey(0)

    def sobelFiltering(self):
        # Load the image and Convert the image to grayscale
        img = cv.imread(ProjectGlobals.FirstSelectedImage, 0)
        # Apply the Sobel operator to the image
        sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
        sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
        # Combine the gradient magnitudes along the two axes
        sobel = sobelX + sobelY
        # Save the resulting image
        # cv.imshow('sobelX', sobelX)
        # cv.imshow('sobelY', sobelY)
        cv.imshow('After sobel filter', sobel)
        updateTheProcessedImage(sobel)
        cv.waitKey(0)

    def weightedFiltering(self):
        # Load the image and Convert the image to grayscale
        img = cv.imread(ProjectGlobals.FirstSelectedImage)
        # Create the Laplacian kernel
        kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
        # Apply the Laplacian filter to the image
        weighted = cv.filter2D(img, -1, kernel)
        # show the resulting image
        cv.imshow('Image Before weighted filter', img)
        cv.imshow('Image after weighted filter', weighted)
        updateTheProcessedImage(weighted)
        cv.waitKey(0)


class FilteringFactory():
    global filteringFunctions
    filteringFunctions = FilteringFunctions()

    @staticmethod
    def startProcessing(operation):
        if (operation == FilteringOperations.averageFilter.value):
            filteringFunctions.averageFiltering()
        if (operation == FilteringOperations.gaussianFilter.value):
            filteringFunctions.gaussianFiltering()
        if (operation == FilteringOperations.medianFilter.value):
            filteringFunctions.medianFiltering()
        if (operation == FilteringOperations.minFilter.value):
            filteringFunctions.minFiltering()
        if (operation == FilteringOperations.maxFilter.value):
            filteringFunctions.maxFiltering()
        if (operation == FilteringOperations.laplacianFilter.value):
            filteringFunctions.laplacianFiltering()
        if (operation == FilteringOperations.laplacianOfGaussianFilter.value):
            filteringFunctions.laplacianOfGaussianFiltering()
        if (operation == FilteringOperations.prewittFilter.value):
            filteringFunctions.prewittFiltering()
        if (operation == FilteringOperations.sobelFilter.value):
            filteringFunctions.sobelFiltering()
        if (operation == FilteringOperations.weightedFilter.value):
            filteringFunctions.weightedFiltering()
