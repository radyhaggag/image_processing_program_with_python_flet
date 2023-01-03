from tkinter.filedialog import askopenfilename

from flet import *
from flet.ref import Ref
from utils.project_globals import ProjectGlobals

from utils.project_assets import ProjectAssets
from utils.project_colors import ProjectColors
from utils.project_size import ProjectSize
from utils.project_strings import ProjectStrings

initialDir = "E:\\Fcai\\Image processing\\Practical project\\assets"


class SelectImageWidget:

    def buildWidget(self, index):
        mainContainerRef = Ref[Container]()
        imageRef = Ref[Image]()
        textRef = Ref[Text]()
        mainColumnRef = Ref[Column]()
        btnRef = Ref[ElevatedButton]()
        if (index == 0):
            mainContainerRef = ProjectGlobals.FirstImageBoxContainerRef
        else:
            mainContainerRef = ProjectGlobals.SecondImageBoxContainerRef
            btnRef = ProjectGlobals.SecondBtnRef

        def changeContainerImage(self):
            selectedImagePath = askopenfilename(initialdir=initialDir)
            if(selectedImagePath == ""):
                return
            mainContainerRef.current.content = Image(
                src=selectedImagePath,
                fit=ImageFit.CONTAIN,
                width=ProjectSize.s400,
                height=ProjectSize.s400,
            )
            if (index == 0):
                ProjectGlobals.FirstSelectedImage = selectedImagePath
            else:
                ProjectGlobals.SecondSelectedImage = selectedImagePath

            mainContainer.update()
            mainColumnRef.current.controls = [
                mainContainer,
                removeBtn,
            ]
            mainColumnRef.current.update()

        def removeSelectedImage(self):
            if (index == 0):
                ProjectGlobals.FirstSelectedImage = ProjectAssets.vectorImage
            else:
                ProjectGlobals.SecondSelectedImage = ProjectAssets.vectorImage

            mainContainerRef.current.content = Column(
                controls=[
                    mainImage,
                    mainText,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
            mainContainer.update()
            mainColumnRef.current.controls = [
                mainContainer,
                Container(height=ProjectSize.s45),
            ]
            mainColumnRef.current.update()

        mainContainer = Container(
            ref=mainContainerRef,
            width=ProjectSize.s400,
            height=ProjectSize.s400,
            bgcolor=ProjectColors.grey,
            border_radius=ProjectSize.s5,
            border=border.all(
                color=ProjectColors.orange,
                width=ProjectSize.s3,
            ),
            on_click=lambda _: changeContainerImage(self=self)
        )
        mainText = Text(
            ProjectStrings.selectImageMessage + "\t #" + str(index + 1),
            color=ProjectColors.black,
            ref=textRef,
        )
        mainImage = Image(
            src=ProjectAssets.vectorImage,
            ref=imageRef,
            height=ProjectSize.s300,
        )
        mainContainer.content = Column(
            controls=[
                mainImage,
                mainText,
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

        removeBtn = ElevatedButton(
            ref=btnRef,
            text=ProjectStrings.removeImage,
            icon=icons.CLOSE,
            color=ProjectColors.white,
            bgcolor=ProjectColors.red,
            on_click=lambda _: removeSelectedImage(self=self),
            height=ProjectSize.s45,
            width=ProjectSize.s200,
        )

        return Column(
            ref=mainColumnRef,
            controls=[
                mainContainer,
                Container(height=ProjectSize.s45),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
        )


def getImage(imageSrc):
    return Image(
        src=imageSrc,
        fit=ImageFit.CONTAIN,
    )
