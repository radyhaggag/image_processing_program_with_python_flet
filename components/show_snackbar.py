from flet import SnackBar, Text
from utils.project_globals import ProjectGlobals

def showSnackBar(str, color):
    ProjectGlobals.page.snack_bar = SnackBar(
        Text(str),
        bgcolor=color,
    )
    ProjectGlobals.page.snack_bar.open = True
    ProjectGlobals.page.update()
