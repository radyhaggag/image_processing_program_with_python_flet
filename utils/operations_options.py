from flet import dropdown

from utils.project_enums import ArithmeticOperations, FilteringOperations, HistogramOperations, ImageConversionOperations, MainOperations, SpatialDomainOperations


class OperationsOptions():
    mainOperations = [
        dropdown.Option(MainOperations.imageConversion.value),
        dropdown.Option(MainOperations.extractROI.value),
        dropdown.Option(MainOperations.arithmetic.value),
        dropdown.Option(MainOperations.spatialDomain.value),
        dropdown.Option(MainOperations.histogram.value),
        dropdown.Option(MainOperations.filtering.value),
        dropdown.Option(MainOperations.threshold.value),
        dropdown.Option(MainOperations.resizeImage.value),
    ]
    imageConversionOperations = [
        dropdown.Option(ImageConversionOperations.imageToGrayScale.value),
        dropdown.Option(ImageConversionOperations.imageToBinary.value),
        dropdown.Option(ImageConversionOperations.imageToRGB.value),
    ]
    arithmeticOperations = [
        dropdown.Option(ArithmeticOperations.addition.value),
        dropdown.Option(ArithmeticOperations.subtraction.value),
        dropdown.Option(ArithmeticOperations.bitwiseAnd.value),
        dropdown.Option(ArithmeticOperations.bitwiseOr.value),
        dropdown.Option(ArithmeticOperations.bitwiseXor.value),
        dropdown.Option(ArithmeticOperations.bitwiseNot.value),
    ]
    transformationOperations = [
        dropdown.Option(SpatialDomainOperations.identityTransformation.value),
        dropdown.Option(SpatialDomainOperations.intensitySlicing.value),
        dropdown.Option(SpatialDomainOperations.logTransformation.value),
        dropdown.Option(SpatialDomainOperations.contrastStretching.value),
        dropdown.Option(SpatialDomainOperations.negativeTransformation.value),
        dropdown.Option(SpatialDomainOperations.powerLawTransformation.value),
    ]
    histogramOperations = [
        dropdown.Option(HistogramOperations.histogramCalculation.value),
        dropdown.Option(HistogramOperations.histogramEqualization.value),
    ]
    filteringOperations = [
        dropdown.Option(FilteringOperations.averageFilter.value),
        dropdown.Option(FilteringOperations.gaussianFilter.value),
        dropdown.Option(FilteringOperations.medianFilter.value),
        dropdown.Option(FilteringOperations.minFilter.value),
        dropdown.Option(FilteringOperations.maxFilter.value),
        dropdown.Option(FilteringOperations.laplacianFilter.value),
        dropdown.Option(
            FilteringOperations.laplacianOfGaussianFilter.value,
        ),
        dropdown.Option(FilteringOperations.sobelFilter.value),
        dropdown.Option(FilteringOperations.prewittFilter.value),
        dropdown.Option(FilteringOperations.weightedFilter.value),
    ]
