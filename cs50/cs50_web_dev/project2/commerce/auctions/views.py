from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import User, Auction, AuctionForm, Categorie, BidForm, Watchlist, Comments, CommentsForm



def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def auction(request, auction_id):
    auction = Auction.objects.get(id=auction_id)
    user = request.user
    watchlists = Watchlist.objects.all()
    watchlist_check = False
    for watchlist in watchlists:
        if watchlist.auction == auction and watchlist.user == request.user:
            watchlist_check = True
    if request.method == "POST":
        post = True
        return render(request, "auctions/auction.html", {
            "auction": auction,
            "post": post,
            "form": BidForm(),
            "watchlist_check": watchlist_check,
            "comments": Comments.objects.all()
        })
    post = False
    return render(request, "auctions/auction.html", {
        "auction": auction,
        "post": post,
        "form": BidForm(),
        "watchlist_check": watchlist_check,
        "comments": Comments.objects.all()
    })

@login_required(login_url="/login")
def new(request):
    if request.method == "POST":
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction_user = request.user
            auction_title = form.cleaned_data["auction_title"]
            auction_description = form.cleaned_data["auction_description"]
            auction_picture = form.cleaned_data["auction_picture"]
            starting_price = form.cleaned_data["starting_price"]
            categorie = form.cleaned_data["categorie"]

            auction = Auction()
            auction.auction_user = auction_user
            auction.auction_title = auction_title
            auction.auction_description = auction_description
            auction.auction_picture = auction_picture
            auction.starting_price = starting_price
            auction.current_price = starting_price
            auction.categorie = categorie
            auction.save()

    return render(request, "auctions/new.html", {
        "form": AuctionForm()
    })

@login_required(login_url="/login")
def bid(request, auction_id):
    auction = Auction.objects.get(id=auction_id)
    auction_user = request.user
    current_price = auction.current_price
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            new_price = form.cleaned_data["current_price"]
            if new_price > current_price:
                auction.current_price = new_price
                auction.winning_user = auction_user
                auction.save()
                return render(request, "auctions/bid.html", {
                "message": "Bid added successfully.",
                "auction_id": auction_id
                })
            else:
                return render(request, "auctions/bid.html", {
                "message": "Error: Your bid need to be higher then current price.",
                "auction_id": auction_id
                })
    return render(request, "auctions/bid.html")

@login_required(login_url="/login")
def watchlist(request):
    user = request.user
    watchlists = Watchlist.objects.all()
    if request.method == "POST":
        auction_id = request.POST["auction"]
        auction = Auction.objects.get(id=auction_id)
        function = request.POST["function"]
        if function == "add":
            watchlist = Watchlist()
            watchlist.auction = auction
            watchlist.user = user
            watchlist.save()
        if function == "remove":
            for watchlist in watchlists:
                if watchlist.auction == auction and watchlist.user == user:
                    watchlist.delete()
        return redirect("auction", auction_id=auction)
    
    return render(request, "auctions/watchlist.html", {
        "auctions": Auction.objects.all(),
        "watchlists": watchlists
    })

@login_required(login_url="/login")
def comment(request, auction_id):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            auction_user = request.user
            auction = Auction.objects.get(id=auction_id)
            comment = form.cleaned_data["comment"]

            comments = Comments()
            comments.user = auction_user
            comments.auction = auction
            comments.comment = comment
            comments.save()
        return redirect("auction", auction_id=auction)
    return render(request, "auctions/comment.html", {
        "form": CommentsForm(),
        "auction_id": auction_id,
    })

@login_required(login_url="/login")
def end(request):
    if request.method == "POST":
        auction_id = request.POST["auction"]
        auction = Auction.objects.get(id=auction_id)

        auction.active = False
        auction.save()
    return redirect("auction", auction_id=auction_id)

def archive(request):
    return render(request, "auctions/archive.html", {
        "auctions": Auction.objects.all()
    })

def user_listings(request):
    return render(request, "auctions/user_listings.html", {
        "auctions": Auction.objects.all()
    })