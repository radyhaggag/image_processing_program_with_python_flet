from flet.ref import Ref
from flet import Column, Container, ElevatedButton, page

from utils.project_assets import ProjectAssets

class ProjectGlobals:
    FirstSelectedImage = ProjectAssets.vectorImage
    SecondSelectedImage = ProjectAssets.vectorImage
    mainColumnRef = Ref[Column]()
    FirstImageBoxContainerRef = Ref[Container]()
    SecondImageBoxContainerRef = Ref[Container]()
    SecondBtnRef = Ref[ElevatedButton]()
    processedImage = ''
    page = page
