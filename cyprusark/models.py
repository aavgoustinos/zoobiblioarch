from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=50)
    slider_description = models.CharField(max_length=100)
    slider_image = models.FileField(null=True, blank=True, upload_to="slider_images/")
    order = models.IntegerField()
    slug = models.CharField(max_length=100)
    online = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Collection Model

class Collection(models.Model):

    
    collection_name = models.CharField(max_length=30,default=None,unique=True, help_text='<h3>The name of the Museum(e.g., The Met Museum )</h3>')
    
    photo = models.ImageField(null=True, blank=True, upload_to="collection_images/")
    
    description = RichTextField(null=True, blank=True,max_length=10000,default=None)
    
    sameAs  = models.URLField(max_length = 200,blank=True,)
    
    slug = models.SlugField(max_length = 100)

    order = models.IntegerField()

    online = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = 'Collection'
    def __str__(self):
     return self.collection_name  

# Museum Model

class Museum(models.Model):
   
    
    museum_name = models.CharField(max_length=50,default=None,unique=True, help_text='<h3>The name of the Museum(e.g., The Met Museum )</h3>')
   
    working_hours= models.CharField(max_length=30,default=None)
   
    address = models.CharField(null=True, blank=True,max_length=50,default=None)
   
    city = models.CharField(null=True, blank=True,max_length=30,default=None)
    
    country = models.CharField(null=True, blank=True,max_length=80,default=None)
    
    logo = models.ImageField(upload_to='museum/museum_logo_images')
   
    phone = models.CharField(null=True, blank=True,max_length=80,default=None)
   
    description = RichTextField(null=True, blank=True,max_length=10000,default=None)
   
    museum_website  = models.URLField(null=True, blank=True,max_length = 200)

    sameAs  = models.URLField(null=True, blank=True,max_length = 200)

    online = models.BooleanField("Online",default=True)
   
    slug = models.SlugField(max_length = 100)
    
    
    
    class Meta:
        verbose_name = 'Museum'
    def __str__(self):
     return self.museum_name



# Museum_item Model

class Museum_Item(models.Model):
    

   
    TYPE = (
       
        ('Unknown','Unknown'),    
        ('Drawing', 'Drawing'),
        ('Book', 'Book'),
        ('Map', 'Map'),
        ('Painting', 'Painting'),
        ('Photograph', 'Photograph'),
        ('Manuscripts', 'Manuscripts'),
        ('Posters', 'Posters'),
        ('Sculptures', 'Sculptures'),
        ('VisualArtwork', 'VisualArtwork'), 
        ('Vases', 'Vases'),
        ('Bronzes', ' Bronze'),
        ('Terracottas','Terracottas'),
        ('Coins', 'Coins'),
        ('Paintings-Icons', 'Paintings-Icons'),
         
    )
    
    title = models.CharField(null=True, blank=True,max_length=60,unique=True)
    
    classification = models.CharField(null=True, blank=True,max_length=60, choices=TYPE)
    
    date = models.CharField(null=True, blank=True,max_length=30)
    
    description = RichTextField(null=True,blank=True,max_length=10000)
 
    image_one = models.ImageField(null=True, blank=True,upload_to='museum_items/image_one_items')
   
    image_two = models.ImageField(null=True, blank=True,upload_to='museum_items/image_two_items')
    
    dimensions = models.CharField(null=True, blank=True,max_length=50)
    
    creditline = models.CharField(null=True, blank=True,max_length=60)
    
    accession_number = models.CharField(null=True, blank=True,max_length=60)
    
    sameAs  = models.URLField(null=True, blank=True,max_length = 200)
    
    culture= models.CharField(null=True, blank=True,max_length=30)
    
    medium = models.CharField(null=True, blank=True,max_length=30)
    
    period = models.CharField(null=True, blank=True,max_length=30)
    
    rights_reproduction= models.CharField(null=True, blank=True,max_length=130)
    
    # Admin
    #  
    online = models.BooleanField("Online",default=True)
    
    slug = models.SlugField(null=True, blank=True,max_length = 100)

    order = models.IntegerField()


    # One to ManyToMany
   
    collection = models.ManyToManyField(Collection,null=True)
   
    class Meta:
        verbose_name = 'Museum item'
    def __str__(self):
            return self.title 
     
    def admin_photo(self):
        
        return mark_safe('<img src="{}" height="180", width="150"/>'.format(self.image_one.url))
    
    def __str__(self):
        return self.title