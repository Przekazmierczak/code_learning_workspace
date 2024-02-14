from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm, Textarea

class User(AbstractUser):
    pass

class Categorie(models.Model):
    categories = models.CharField(default=None, max_length=200)

    def __str__(self):
        return self.categories

class Auction(models.Model):
    auction_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction_owner")
    auction_title = models.CharField(max_length=200)
    auction_description = models.CharField(max_length=2000)
    auction_picture = models.URLField(default=None, blank=True)
    starting_price = models.DecimalField(decimal_places=2, max_digits=9)
    current_price = models.DecimalField(decimal_places=2, max_digits=9)
    winning_user = models.ForeignKey(User, on_delete=models.PROTECT, default=None, null=True, related_name="winning_user")
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, default=None, related_name="categorie")
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

class Comments(models.Model):
    comment = models.CharField(max_length=5000)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ["auction_title", "auction_description", "auction_picture", "starting_price", "categorie"]
        widgets = {
            "auction_description": Textarea(attrs={"cols": 80, "rows": 20}),
        }

class BidForm(ModelForm):
    class Meta:
        model = Auction
        fields = ["current_price"]

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["comment"]
        widgets = {
            "comment": Textarea(attrs={"cols": 50, "rows": 10}),
        }