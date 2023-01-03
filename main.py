import flet as ft
from components.select_operations_form import SelectOperationsForm

from components.select_image_widget import SelectImageWidget
from utils.project_colors import ProjectColors
from utils.project_globals import ProjectGlobals
from utils.project_size import ProjectSize
from utils.project_strings import ProjectStrings

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


def main(page: ft.page):
    page.title = ProjectStrings.projectName
    page.bgcolor = ProjectColors.white
    page.window_width = ProjectSize.s1000
    page.window_height = ProjectSize.s800
    # page.window_resizable = False
    ProjectGlobals.page = page
    themeMode = ft.ThemeMode(value=ft.ThemeMode.LIGHT)
    page.theme_mode = themeMode
    page.add(ft.Column(
        ref=ProjectGlobals.mainColumnRef,
        controls=[
            ft.Row(
                controls=[
                    SelectImageWidget.buildWidget(self=None, index=0),
                    SelectImageWidget.buildWidget(self=None, index=1),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            SelectOperationsForm(),
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ))
    ProjectGlobals.SecondImageBoxContainerRef.current.width = 0.0
    ProjectGlobals.SecondImageBoxContainerRef.current.update()

ft.app(target=main, assets_dir='assets')
