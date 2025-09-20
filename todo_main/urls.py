
from django.urls import include, path
from .views import *

urlpatterns = [
    path("", task_read, name="home"),
    # path("update/<int:pk>", task_update),
    path("add/", task_add, name="task_add"),
    path("delete/<int:pk>", task_delete, name="task_delete")
]