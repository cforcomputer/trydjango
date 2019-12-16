from django.shortcuts import render

from .forms import TextbookForm
from .models import Textbook
# Create your views here.
# create under textbooks instead of pages because congruency
# everything under the textbooks 'view' should be contained within
# textbooks

# def textbook_create_view(request):
#     form = TextbookForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = TextbookForm()
#     context = {
#         'form': form
#     }
#     return render(request, "textbooks/textbook_create.html", context)

def textbook_create_view(request):
    print(request.GET)
    print(request.POST)
    my_new_title = request.POST.get('title')
    print(my_new_title)
    context = {}
    return render(request, "textbooks/textbook_create.html", context)

def question_detail_view(request):
    obj = Textbook.objects.get(id=3)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj # context variable is object
    }
    return render(request, "textbooks/textbook_detail.html", context)
