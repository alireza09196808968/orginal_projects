######################################################################################################
#--------------------------------------------Import-Section------------------------------------------#
######################################################################################################
from django.urls import path, re_path
from . import views
######################################################################################################
#--------------------------------------------Code_Execution------------------------------------------#
######################################################################################################
app_name = "Books"
urlpatterns = [
    path("", views.index, name = "index"),
    path("listView", views.BookListView.as_view(), name = "listView")
]
