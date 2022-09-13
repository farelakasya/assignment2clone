from gettext import Catalog
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_katalog(request):
    list_of_katalogs = CatalogItem.objects.all()
    context = {
        'name' : 'Farel Rishad Akasya',
        'student_Id' : '2106631646',
        'list_katalog' : list_of_katalogs
    }
    return render(
        request,
        'katalog.html',
        context
    )