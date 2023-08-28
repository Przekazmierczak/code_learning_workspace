from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("<int:user_id>", views.profile, name="profile"),
    path("following", views.following, name="following"),

    path("post/<int:post_id>", views.get_post, name="get_post"),
    path("api/post/<int:post_id>/", views.update_post, name="update_post"),
]
