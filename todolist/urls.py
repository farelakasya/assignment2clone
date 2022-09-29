from django.urls import path
from todolist.views import (
    register_user,
    login_user,
    logout_user,
    show_todolist,
    create_task,
    delete_task,
    update_task,
)

app_name = "todolist"
urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("create-task/", create_task, name="create_task"),
    path("logout/", logout_user, name="logout"),
    path("delete-task/<str:id>/", delete_task, name="delete_task"),
    path("update-finished/<str:id>/", update_task, name="update_task"),
]