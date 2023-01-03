import flet as ft

from utils.project_colors import ProjectColors
from utils.project_size import ProjectSize


class CustomButton(ft.UserControl):
    def __init__(self, icon, text, onClick):
        super().__init__()
        self.icon = icon
        self.text = text
        self.onClick = onClick

    def build(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(self.icon, color=ProjectColors.red),
                    ft.Text(self.text, color=ProjectColors.black),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            border_radius=ProjectSize.s5,
            bgcolor=ProjectColors.grey,
            padding=ProjectSize.s10,
            width=ProjectSize.s200,
            alignment=ft.alignment.center,
            border=ft.border.all(
                color=ProjectColors.darkGrey,
                width=ProjectSize.s1,
            ),
            on_click=self.onClick
        )
