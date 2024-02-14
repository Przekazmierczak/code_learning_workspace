from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("create", views.create, name="create"),
    path("edit", views.edit, name="edit"),
    path("random_page", views.random_page, name="random_page")
]
