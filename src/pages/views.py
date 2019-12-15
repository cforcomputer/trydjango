from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# A place that handles your various webpages
# using functions or classes written in python
def home_view(request, *args, **kwargs): # args kwargs --> look up in python
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {}) # returns html doc

def contact_view(request, *args, **kwargs): # args kwargs --> look up in python
    return render(request, "textbook.html", {}) # returns html doc

def textbook_view(request, *args, **kwargs): # q and a for textbooks
    my_context = {
        "title": "this is a title in views.py",
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 332, 312, "abs"],
        "my_html": "<h1>Hello world</h1>"
    }
    return render(request, "textbook.html", my_context)