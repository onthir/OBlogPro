from django.shortcuts import render
from .models import *
from master.models import *
# Create your views here.
def home(request):
    categories = Category.objects.all()
    downloads = Download.objects.all()

    context = {
        'categories': categories,
        'downloads': downloads,
    }
    return render(request, 'download/download.html', context)

def details(request, id):
    categories = Category.objects.all()
    objects = Download.objects.get(id=id)
    context = {
        'objects': objects,
        'categories': categories
    }
    return render(request, 'download/details.html', context)