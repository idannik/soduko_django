from django.urls import path

from soduko.board.views import get_board


app_name = "board"

urlpatterns = [
    path("get_board/", view=get_board, name="get_board"),
]
