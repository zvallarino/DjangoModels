from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Painting(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey("Artist",  on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=600)
    isbn = models.CharField('ISBN',max_length=13, unique=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("painting_detail", kwargs={"pk": self.pk})
    

class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True,blank=True, auto_now=False, auto_now_add=False)
    
    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} was born on {self.date_of_birth}'
    
import uuid

class PaintingInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    painting = models.ForeignKey("Painting", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField( max_length=200)
    due_back = models.DateField( auto_now=False, auto_now_add=False,null = True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,null = True, blank=True)

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a','Avaiable'),
        ('r','Reserved'),
    )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')
    
    class Meta:
        ordering = ['due_back']
        
    def __str__(self):
        return f'{self.id} {self.painting.title}'
    