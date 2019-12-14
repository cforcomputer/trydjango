from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# A place that handles your various webpages
# using functions or classes written in python
def home_view(request, *args, **kwargs): # args kwargs --> look up in python
    return HttpResponse("<h1>Hello World</h1>") # string of HTML code

def contact_view(request, *args, **kwargs): # args kwargs --> look up in python
    return HttpResponse("<h1>Contact swab</h1>") # string of HTML code