from django.contrib import admin
from .models import User, Auction, Categorie, Watchlist, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Categorie)
admin.site.register(Watchlist)
admin.site.register(Comments)