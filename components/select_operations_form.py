from flet import *
from flet.ref import Ref
from components.custom_button import CustomButton
from components.show_resize_dialog import showResizeInputsDialog
from components.show_threshold_dialog import showThresholdInputDialog
from functions.extract_roi_function import ExtractROIFunction
from functions.image_conversion_functions import ImageConversionFactory
from components.show_saving_dialog import showInputSavePathDialog
from functions.threshold_function import ThresholdFunction
from utils.project_assets import ProjectAssets
from utils.project_globals import ProjectGlobals

from utils.project_size import ProjectSize
from utils.project_colors import ProjectColors
from utils.project_strings import ProjectStrings
from utils.operations_options import MainOperations, OperationsOptions
from functions.spatial_domain_functions import TransformationFactory
from functions.filtering_functions import FilteringFactory
from functions.histogram_functions import HistogramFactory
from functions.arithmetic_functions import ArithmeticFactory


class SelectOperationsForm(UserControl):
    def build(self):
        mainContainerRef = Ref[Container]()
        subContainerRef = Ref[Container]()
        mainDropdownRef = Ref[Dropdown]()
        subDropdownRef = Ref[Dropdown]()
        mainContainer = Container(
            ref=mainContainerRef,
            width=ProjectSize.s300,
            padding=ProjectSize.s10,
            # border_radius=ProjectSize.s5,
            # border=border.all(
            #     color=ProjectColors.orange,
            #     width=ProjectSize.s1,
            # ),
        )
        global mainOperation
        mainOperation = ""
        global subOperation
        subOperation = ""

        def onSubOperationChange(self, operation):
            global subOperation
            subOperation = operation.data

        subOperationDropdown = buildOperationsDropDown(
            ref=subDropdownRef,
            label=ProjectStrings.subOperation,
            self=self,
            onChange=lambda e: onSubOperationChange(self=self, operation=e),
            options=None,
        )

        def onArithmeticSelected():
            subDropdownRef.current.options = OperationsOptions.arithmeticOperations
            ProjectGlobals.SecondImageBoxContainerRef.current.width = ProjectSize.s400
            ProjectGlobals.SecondImageBoxContainerRef.current.update()
            if (ProjectGlobals.SecondSelectedImage != ProjectAssets.vectorImage):
                ProjectGlobals.SecondBtnRef.current.width = ProjectSize.s200
                ProjectGlobals.SecondBtnRef.current.update()

        def mainActionWhenSelectOperation():
            ProjectGlobals.SecondImageBoxContainerRef.current.width = 0
            ProjectGlobals.SecondImageBoxContainerRef.current.update()
            if (ProjectGlobals.SecondSelectedImage != ProjectAssets.vectorImage):
                ProjectGlobals.SecondBtnRef.current.width = 0
                ProjectGlobals.SecondBtnRef.current.update()

        def onMainOperationChange(self, operation):
            global mainOperation
            mainOperation = operation.data
            if (operation.data == MainOperations.arithmetic.value):
                onArithmeticSelected()
            else:
                mainActionWhenSelectOperation()
            if (mainOperation == MainOperations.extractROI.value or
                mainOperation == MainOperations.threshold.value or
                    mainOperation == MainOperations.resizeImage.value):
                subContainerRef.current.content = None
                subContainer.update()
                return
            if (mainOperation == MainOperations.imageConversion.value):
                subDropdownRef.current.options = OperationsOptions.imageConversionOperations
            if (mainOperation == MainOperations.spatialDomain.value):
                subDropdownRef.current.options = OperationsOptions.transformationOperations
            if (mainOperation == MainOperations.histogram.value):
                subDropdownRef.current.options = OperationsOptions.histogramOperations
            if (mainOperation == MainOperations.filtering.value):
                subDropdownRef.current.options = OperationsOptions.filteringOperations
            subContainerRef.current.content = subOperationDropdown
            subContainer.update()

        mainOperationsDropdown = buildOperationsDropDown(
            ref=mainDropdownRef,
            label=ProjectStrings.operation,
            self=self,
            options=OperationsOptions.mainOperations,
            onChange=lambda operation: onMainOperationChange(
                self=self,
                operation=operation,
            )
        )

        def startProcessing(self):
            if (ProjectGlobals.FirstSelectedImage == ProjectAssets.vectorImage):
                return
            if (mainOperation == MainOperations.imageConversion.value):
                ImageConversionFactory.startProcessing(operation=subOperation)
            if (mainOperation == MainOperations.extractROI.value):
                ExtractROIFunction.extractROI()
            if (mainOperation == MainOperations.arithmetic.value):
                ArithmeticFactory.startProcessing(operation=subOperation)
            if (mainOperation == MainOperations.spatialDomain.value):
                TransformationFactory.startProcessing(operation=subOperation)
            if (mainOperation == MainOperations.histogram.value):
                HistogramFactory.startProcessing(operation=subOperation)
            if (mainOperation == MainOperations.filtering.value):
                FilteringFactory.startProcessing(operation=subOperation)
            if (mainOperation == MainOperations.threshold.value):
                # Show the dialog for take threshold value
                # after that the threshold function will called
                showThresholdInputDialog(self)
            if (mainOperation == MainOperations.resizeImage.value):
                # Show the dialog for take width and height values
                # after that the resize function will called
                showResizeInputsDialog(self)

        subContainer = Container(ref=subContainerRef)
        mainContainer.content = Column(
            controls=[
                mainOperationsDropdown,
                subContainer,
                CustomButton(
                    icons.PLAY_CIRCLE_FILL_OUTLINED,
                    ProjectStrings.start,
                    lambda _: startProcessing(self=self),
                ),
                CustomButton(
                    icons.SAVE,
                    ProjectStrings.saveImage,
                    lambda _: showInputSavePathDialog(self),
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER,
        )
        return Column(
            controls=[
                mainContainer,
                Container(height=ProjectSize.s40),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )


def buildOperationsDropDown(self, label, ref, options, onChange):
    return Dropdown(
        ref=ref,
        width=ProjectSize.s200,
        hint_text=ProjectStrings.selectOperation,
        label=label,
        color=ProjectColors.black,
        label_style=TextStyle(
            color=ProjectColors.black,
        ),
        options=options,
        on_change=onChange
    )
