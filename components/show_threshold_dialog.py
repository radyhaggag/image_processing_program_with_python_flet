from components.show_snackbar import showSnackBar
from functions.resize_image_function import ResizeImageFunction
from functions.save_image_function import saveImage
from functions.threshold_function import ThresholdFunction
from utils.project_assets import ProjectAssets
from utils.project_size import ProjectSize
from utils.project_globals import ProjectGlobals
import cv2 as cv
import flet as ft

from utils.project_strings import ProjectStrings


global thresholdValue


def showThresholdInputDialog(self):
    global thresholdValue
    thresholdValue = 127

    def close_dlg(e):
        dlg_modal.open = False
        ProjectGlobals.page.update()
        ThresholdFunction.threshold(thresholdValue)

    def onFieldValChanged(e):
        global thresholdValue
        thresholdValue = int(e.control.value)


    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(ProjectStrings.thresholdMsg),
        content=ft.TextField(
            hint_text=ProjectStrings.threshold,
            on_change=lambda e: onFieldValChanged(e),
            expand=True,
        ),
        actions=[
            ft.TextButton(ProjectStrings.threshold, on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    ProjectGlobals.page.dialog = dlg_modal
    dlg_modal.open = True
    ProjectGlobals.page.update()
