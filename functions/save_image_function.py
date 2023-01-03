import cv2 as cv
from flet import colors
from utils.project_assets import ProjectAssets
from utils.project_globals import ProjectGlobals
from utils.project_strings import ProjectStrings
from components.show_snackbar import showSnackBar


# Save the image with openCv
def saveImage(imagePath):
    try:
        fullImagePath = ProjectAssets.savingPath + imagePath
        cv.imwrite(fullImagePath, ProjectGlobals.processedImage)
        print(ProjectAssets.savingPath + imagePath)
        showSnackBar(ProjectStrings.imageSavedSuccess, colors.GREEN)
    except:
        showSnackBar(ProjectStrings.imageSavedFailed, colors.RED)
        print(imagePath)


def updateTheProcessedImage(newImage):
    ProjectGlobals.processedImage = newImage
