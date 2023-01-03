from components.show_snackbar import showSnackBar
from functions.resize_image_function import ResizeImageFunction
from functions.save_image_function import saveImage
from utils.project_assets import ProjectAssets
from utils.project_size import ProjectSize
from utils.project_globals import ProjectGlobals
import cv2 as cv
import flet as ft

from utils.project_strings import ProjectStrings


global width, height


def showResizeInputsDialog(self):
    global width, height
    width = 0
    height = 0

    def close_dlg(e):
        dlg_modal.open = False
        ProjectGlobals.page.update()
        ResizeImageFunction.resize(width, height)

    def onWidthFieldValueChange(e):
        global width
        width = int(e.control.value)

    def onHeightFieldValueChange(e):
        global height
        height = int(e.control.value)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(ProjectStrings.resizeImageMsg),
        content=ft.Row(
            height=ProjectSize.s100,
            expand=True,
            controls=[
                ft.TextField(
                    hint_text=ProjectStrings.width,
                    on_change=lambda e: onWidthFieldValueChange(e),
                    expand=True,
                ),
                ft.Container(
                    width=ProjectSize.s10
                ),
                ft.TextField(
                    hint_text=ProjectStrings.height,
                    on_change=lambda e: onHeightFieldValueChange(e),
                    expand=True,
                ),
            ],
        ),
        actions=[
            ft.TextButton(ProjectStrings.resize, on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    ProjectGlobals.page.dialog = dlg_modal
    dlg_modal.open = True
    ProjectGlobals.page.update()
