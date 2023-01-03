from enum import Enum


class MainOperations(Enum):
    imageConversion = "Image Conversion"
    extractROI = "Extract ROI"
    arithmetic = "Arithmetic"
    spatialDomain = "Spatial Domain"
    histogram = "Histogram"
    filtering = "Filtering"
    threshold = "Threshold"
    resizeImage = "Resize image"


class ImageConversionOperations(Enum):
    imageToGrayScale = 'Gray Scale'
    imageToBinary = 'Binary'
    imageToRGB = 'RGB'


class SpatialDomainOperations(Enum):
    identityTransformation = "Identity Transformation"
    negativeTransformation = "Negative Transformation"
    logTransformation = "Log Transformation"
    powerLawTransformation = "Power Law Transformation"
    contrastStretching = "Contrast Stretching"
    intensitySlicing = "Intensity Slicing"


class HistogramOperations(Enum):
    histogramCalculation = "Histogram Calculation"
    histogramEqualization = "Histogram Equalization"


class FilteringOperations(Enum):
    averageFilter = "Average"
    gaussianFilter = "Gaussian"
    medianFilter = "Median"
    minFilter = "Min"
    maxFilter = "Max"
    laplacianFilter = "Laplacian"
    laplacianOfGaussianFilter = "Laplacian Of Gaussian"
    sobelFilter = "Sobel"
    prewittFilter = "Prewitt"
    weightedFilter = "Weighted Filter"


class ArithmeticOperations(Enum):
    addition = "Addition"
    subtraction = "Subtraction"
    bitwiseAnd = "Bitwise And"
    bitwiseOr = "Bitwise Or"
    bitwiseXor = "Bitwise Xor"
    bitwiseNot = "Bitwise Not"
