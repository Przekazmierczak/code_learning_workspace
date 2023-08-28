import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Follows, PostForm


def index(request):
    reverse_order = Post.objects.all().order_by('-date')

    # Check if user liked post
    like_check_list = []
    for reverse_order_element in reverse_order:
        like_check = reverse_order_element.users_like.filter(id=request.user.id).exists()
        like_check_list_element = [reverse_order_element, like_check]
        like_check_list.append(like_check_list_element)

    # Poginator
    post_list = like_check_list
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "form":PostForm(),
        "page_obj": page_obj,
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required(login_url="/login")
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            post = form.cleaned_data["post"]
            likes = 0
        
            posts = Post()
            posts.user = user
            posts.post = post
            posts.likes = likes
            posts.save()
    return redirect("index")

def profile(request, user_id):
    if request.method == "POST":
        follow_status = request.POST["follow_status"]
        if follow_status == "Follow":
            logged_user = request.user
            profile_user = User.objects.get(id=user_id)

            follows = Follows()
            follows.user = logged_user
            follows.user_follows = profile_user
            follows.save()
        else:
            follows = get_object_or_404(Follows, user=request.user, user_follows=user_id)
            follows.delete()
    # check follows amount
    follows = Follows.objects.filter(user_follows=user_id).count()
    following = Follows.objects.filter(user=user_id).count()
    # check if user following another user
    if request.user.is_authenticated:
        follows_check = Follows.objects.filter(user=request.user, user_follows=user_id).exists()
    else:
        follows_check = None
    user_posts = Post.objects.filter(user_id=user_id).order_by('-date')
    
    # Poginator
    post_list = user_posts
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "network/profile.html", {
        "user_profile": User.objects.get(id=user_id),
        "user_posts": user_posts,
        "user_id": user_id,
        "follows_check": follows_check,
        "follows": follows,
        "following": following,
        "page_obj": page_obj,
    })

@login_required(login_url="/login")
def following(request):
    
    followed_users = Follows.objects.filter(user=request.user)
    followed_users_list = []
    for followed_user in followed_users:
        followed_users_list.append(followed_user.user_follows)
    followed_users_posts = Post.objects.filter(user__in=followed_users_list).order_by('-date')
    # Check if user liked post
    like_check_list = []
    for followed_users_post in followed_users_posts:
        like_check = followed_users_post.users_like.filter(id=request.user.id).exists()
        like_check_list_element = [followed_users_post, like_check]
        like_check_list.append(like_check_list_element)
    
    # Poginator
    post_list = like_check_list
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print(page_obj)
    
    return render(request, "network/following.html", {
        "form":PostForm(),
        "page_obj": page_obj,
    })

@csrf_exempt
def get_post(request, post_id):
    try:
        get_post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "GET":
        return JsonResponse(get_post.serialize())

    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("post") is not None:
            get_post.post = data["post"]
        get_post.save()
        return HttpResponse(status=204)
    
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

@csrf_exempt
@login_required(login_url="/login")
def update_post(request, post_id):
    if request.method == 'PUT':
        try:
            like_update = Post.objects.get(pk=post_id)
            print(like_update)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Object not found"}, status=404)
    data = json.loads(request.body)
    input_like_ids = data.get('input_like', [])
    like_update.users_like.set(input_like_ids)
    like_update.save()

    return JsonResponse({"message": "Object updated successfully"})