from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:auction_id>", views.auction, name="auction"),
    path("new", views.new, name="new"),
    path("<int:auction_id>/bid", views.bid, name="bid"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("<int:auction_id>/comment", views.comment, name="comment"),
    path("end", views.end, name="end"),
    path("archive", views.archive, name="archive"),
    path("user_listings", views.user_listings, name="user_listings"),
]
