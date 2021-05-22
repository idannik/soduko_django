from django.urls import path

from soduko.board.views import get_board

app_name = "users"
urlpatterns = [
    path("get_board/", view=get_board, name="get_board"),
    # path("update_update/", view=user_update_view, name="update"),
]
