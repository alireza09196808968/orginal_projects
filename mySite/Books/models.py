######################################################################################################
#--------------------------------------------Import-Section------------------------------------------#
######################################################################################################

from django.db import models
import uuid
######################################################################################################
#--------------------------------------------Code-Execution------------------------------------------#
######################################################################################################
# Create your models here.

# this is the Genre of the books Model
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text = "Enter book's genre")

    def __str__(self):
        return self.name

# this is the Book Model
class Book(models.Model):
    title = models.CharField(max_length=200, help_text = "Enter book's title")
    summary = models.TextField(max_length=1000, help_text = "Enter book's summary")
    isbn = models.CharField(max_length=13, help_text = "Enter book's isbn")
    genre = models.ManyToManyField(Genre, help_text = "book-genre relation")
    """
    the additional table is created by Django and we don't need to create it.
    """


    author = models.ForeignKey("Author", on_delete = models.SET_NULL, null = True)
    """
    this is one-to-many relation
    """
    
    def display_genre(self):
        # use to display geners of books
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = "Genre"

    def __str__(self):
        return self.title

# this is the Author Model
class Author(models.Model):
    firstName = models.CharField(max_length=100 )
    lastName = models.CharField(max_length=100)
    dataOfBirth = models.DateField(null = True, blank=True)
    dataOfDeath = models.DateField("Died", blank=True, null=True)
    class Meta:
        ordering = ["lastName", "firstName"]
    def __str__(self):
        return "{0},{1}".format(self.lastName,self.firstName)

# this is the Books instance Model for check availablity
class BookInstance(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,
                         help_text = "Enter primary key"   
                         )
    book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True, null=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ("a", "Available"),
        ("r", "Reserved")
    )
    status = models.CharField(max_length = 1,
                            choices = LOAN_STATUS,
                            blank=True,
                            default = "m",
                            help_text = "Book availablity"
                            )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return "{0},{1}".format(self.id, self.book.title)




