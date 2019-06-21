######################################################################################################
#--------------------------------------------Import-Section------------------------------------------#
######################################################################################################

from django.db import models

######################################################################################################
#--------------------------------------------Code-Execution------------------------------------------#
######################################################################################################
# Create your models here.
# this is the Genre of the books Model

class Genre(models.Model):
    name = models.CharField(max_lenght = 200, help_text = "Enter book's genre")

    def __str__(self):
        return self.name
#this is the Book Model

class Book(models.Model):
    title = models.CharField(max_lenght = 200, help_text = "Enter book's title")
    summary = models.TextField(max_lenght = 1000, help_text = "Enter book's summary")
    isbn = models.CharField(max_lenght = 13, help_text = "Enter book's isbn")
    genre = models.ManyToManyField(Genre, help_text = "book-genre relation")
    """
    the additional table is created by Django and we don't need to create it.
    """

    def __str__(self):
        return self.title