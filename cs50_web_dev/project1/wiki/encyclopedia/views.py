from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect
import os
import random
from markdown2 import Markdown

from . import util

class SearchForm(forms.Form):
    search = forms.CharField(label="search", widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))
class CreateForm(forms.Form):
    create_title = forms.CharField(label="Title")
    create_body = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':15, 'cols':80, 'placeholder': 'Support markdown.'}))
class EditForm(forms.Form):
    edit_title = forms.CharField(label="Title")
    edit_body = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':15, 'cols':80, 'placeholder': 'Support markdown.'}))

def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            if util.get_entry(search):
                return redirect("title", title=search)
            else:
                new_entries = []
                entries = util.list_entries()
                for entrie in entries:
                    if search in entrie:
                        new_entries.append(entrie)
                if new_entries:
                    return render(request, "encyclopedia/index.html", {
                        "entries": new_entries,
                        "form": SearchForm(),
                        "title": "Did you mean"
                    })
                else:
                    return render(request, "encyclopedia/index.html", {
                        "form": SearchForm(),
                        "title": "Not Found"
                    })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm(),
        "title": "All Pages"
    })

def title(request, title):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            edit_title = form.cleaned_data["edit_title"]
            edit_body = form.cleaned_data["edit_body"]
            f = open(f"entries/{edit_title}.md", "w")
            f.write(f"{edit_body}")
            f.close
            if edit_title != title:
                os.remove(f"entries/{title}.md")
            return redirect("title", title=edit_title)
    if util.get_entry(title):
        markdowner = Markdown()
        page_body = util.get_entry(title)
        convert_body = markdowner.convert(page_body)
        return render(request, "encyclopedia/page.html", {
            "page_body": convert_body,
            "form": SearchForm(),
            "title": title
        })
    else:
        return render(request, "encyclopedia/page.html", {
            "page_body": "Requested page was not found.",
            "form": SearchForm()
        })

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            create_title = form.cleaned_data["create_title"]
            create_body = form.cleaned_data["create_body"]
            entries = util.list_entries()
            for entrie in entries:
                if entrie == create_title:
                    initial_data = {'create_title': create_title, 'create_body': create_body}
                    return render(request, "encyclopedia/create.html", {
                        "form": CreateForm(initial=initial_data),
                        "message": "Entry already exist"
                        })
            f = open(f"entries/{create_title}.md", "x")
            f.write(f"{create_body}")
            f.close
            return redirect("title", title=create_title)
    return render(request, "encyclopedia/create.html", {
        "form": CreateForm()
    })

def edit(request):
    edit_title = request.POST["title"]
    edit_body = util.get_entry(edit_title)
    initial_data = {'edit_title': edit_title, 'edit_body': edit_body}
    return render(request, "encyclopedia/edit.html", {
        "form": EditForm(initial=initial_data),
        "entry": edit_title
    })

def random_page(request):
    random_entrie = random.choice(util.list_entries())
    return redirect("title", title=random_entrie)
