######################################################################################################
#--------------------------------------------Import-Section------------------------------------------#
######################################################################################################

from django.shortcuts import render
from django.views import generic

from . import models
######################################################################################################
#--------------------------------------------Code-Execution------------------------------------------#
######################################################################################################
# Create your views here.

def index(request):
    context = {

    }
    return render(request ,"Books/index.html", context)
class BookListView(generic.ListView):
    model = models.Book