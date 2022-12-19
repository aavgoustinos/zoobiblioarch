
from sortedm2m.fields import SortedManyToManyField
from django.db import models
from ckeditor.fields import RichTextField

#Article Model
class Article(models.Model):
    
    title = models.CharField(max_length=300,null=True, blank=True,)
    DOI = models.CharField(max_length=200,null=True, blank=True,)
    year = models.IntegerField(null=True, blank=True,)
    abstract = models.TextField(null=True,blank=True,max_length=10000)

    # Journal onetomany
    journal = models.ForeignKey("Journal",on_delete=models.CASCADE,null=True, blank=True,)
   # Journal many to many
    author = SortedManyToManyField("Author")
    keyword = models.ManyToManyField("Keyword",blank=True,)
    region = models.ManyToManyField("Region",blank=True,)


    def __str__(self):
            return f'{self.title},{self.journal}'
    

#Journal Model
class Journal(models.Model):
    
    journal_title = models.CharField(max_length=300,null=True, blank=True,)
    

    def __str__(self):
            return f'{self.journal_title}'

#Keywords Model

class keyword(models.Model):
    
    keyword = models.CharField(max_length=100,null=True, blank=True,)
    

    def __str__(self):
            return f'{self.keyword}'

#Author Model

class Author(models.Model):
    
    first_name = models.CharField(max_length=100,null=True, blank=True,)
    last_name = models.CharField(max_length=100,null=True, blank=True,)
      
    def __str__(self):
            return f'{self.first_name} {self.last_name} {self.id}'
    
#Region Model
class Region(models.Model):
    
    region_name = models.CharField(max_length=100,null=True, blank=True,)
    
      
    def __str__(self):
            return f'{self.region_name}'