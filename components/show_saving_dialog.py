from components.show_snackbar import showSnackBar
from functions.save_image_function import saveImage
from utils.project_assets import ProjectAssets
from utils.project_globals import ProjectGlobals
import cv2 as cv
import flet as ft

from utils.project_strings import ProjectStrings


global imagePath

def showInputSavePathDialog(self):
    if ProjectGlobals.processedImage == '':
        return
    global imagePath
    imagePath = ''

    def close_dlg(e):
        dlg_modal.open = False
        ProjectGlobals.page.update()
        if '.' not in imagePath:
            showSnackBar(ProjectStrings.invalidPathMsg, ft.colors.RED)
        else:
            saveImage(imagePath)

    def onTextFieldValueChange(e):
        global imagePath
        imagePath = e.control.value

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(ProjectStrings.savePathMsg),
        content=ft.TextField(
            hint_text=ProjectStrings.enterThePath,
            on_change=lambda e: onTextFieldValueChange(e),
        ),
        actions=[
            ft.TextButton(ProjectStrings.save, on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    ProjectGlobals.page.dialog = dlg_modal
    dlg_modal.open = True
    ProjectGlobals.page.update()
