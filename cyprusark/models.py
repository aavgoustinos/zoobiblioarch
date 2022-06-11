from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField



# CreativeWork Model

class CreativeWork(models.Model):
    

   
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
        ('Currency', 'Currency'),
        ('Paintings-Icons', 'Paintings-Icons'),
        ('Sculptures', 'Sculpture'),
    )


    MEDIUM = (
       
        ('Unknown','Unknown'),    
        ('Oil on canvas', 'Oil on canvas'),
        ('Oil on wood', 'Oil on wood'),
        ('Limestone', 'Limestone'),

        
        
    )
    
    title = models.CharField(null=True, blank=True,max_length=60,unique=True)
    
    classification = models.CharField(null=True, blank=True,max_length=60, choices=TYPE)
    
    date = models.CharField(null=True, blank=True,max_length=30)
    
    description = RichTextField(null=True,blank=True,max_length=10000)
 
    image_one = models.ImageField(null=False, blank=False,upload_to='creativeworks/image_one_items')
   
    dimensions = models.CharField(null=True, blank=True,max_length=50)
    
    creditline = models.CharField(null=True, blank=True,max_length=60)
    
    accession_number = models.CharField(null=True, blank=True,max_length=60)
    
    sameAs  = models.URLField(null=True, blank=True,max_length = 200)
    
    culture= models.CharField(null=True, blank=True,max_length=30)
    
   
    
    medium =models.CharField(null=True, blank=True,max_length=60, choices=MEDIUM)
    
    period = models.CharField(null=True, blank=True,max_length=30)


    rights_reproduction= models.CharField(null=True, blank=True,max_length=130)
    
    # Admin
    slug = models.SlugField(null=True, blank=True,max_length = 100)

    order = models.IntegerField()

    # One to ManyToMany
   
    bundle = models.ManyToManyField('Bundle')

    maker = models.ForeignKey('Person', on_delete=models.PROTECT,blank=True, null=True)

    online = models.BooleanField("Online",default=True)
   
   
    class Meta:
        verbose_name = 'Creative Work'
    def __str__(self):
            return self.title 
     
    def creative_photo(self):
        
        return mark_safe('<img src="{}" height="100", width="100"/>'.format(self.image_one.url))
    

class Slider(models.Model):
    title = models.CharField(max_length=50)
    slider_description = models.CharField(max_length=100)
    slider_image = models.FileField(null=True, blank=True, upload_to="slider_images/")
    order = models.IntegerField()
    slug = models.CharField(max_length=100)
    online = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def slider_photo(self):
        
        return mark_safe('<img src="{}" height="100", width="100"/>'.format(self.slider_image.url))
    

# Bundle Model

class Bundle(models.Model):

    
    name = models.CharField(max_length=100,default=None,unique=True, help_text='<h3>The name of the Museum(e.g., The Met Museum )</h3>')
    
    photo = models.ImageField(null=True, blank=True, upload_to="bundle_images/")
    
    description = RichTextField(null=True, blank=True,max_length=10000,default=None)
    
    sameAs  = models.URLField(max_length = 200,blank=True,)
    
    slug = models.SlugField(max_length = 100)

    order = models.IntegerField()

    online = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = 'Bundle'
    def __str__(self):

     return self.name  

    def bundle_photo(self):
            
        return mark_safe('<img src="{}" height="100", width="100"/>'.format(self.photo.url))

# Place Model

class Place(models.Model):
   
    TYPE = (
       
        ('CivicStructure','Civic Structure'), 
        ('Museum','Museum'),  
        ('PlaceOfWorship','PlaceOfWorship'), 
        ('Airport','Airport'), 
        ('PlaceOfWorship','PlaceOfWorship'), 

          
        
         
    )
    name = models.CharField(max_length=50,default=None,unique=True, help_text='<h3>The name of the Museum(e.g., The Met Museum )</h3>')

    classification = models.CharField(null=True, blank=True,max_length=60, choices=TYPE)
   
    working_hours= models.CharField(null=True, blank=True,max_length=30,default=None)
   
    address = models.CharField(null=True, blank=True,max_length=50,default=None)
   
    city = models.CharField(null=True, blank=True,max_length=30,default=None)
    
    country = models.CharField(null=True, blank=True,max_length=80,default=None)
    
    logo = models.ImageField(upload_to='logo_images')
   
    phone = models.CharField(null=True, blank=True,max_length=80,default=None)
   
    description = RichTextField(null=True, blank=True,max_length=10000,default=None)
   
    website  = models.URLField(null=True, blank=True,max_length = 200)

    sameAs  = models.URLField(null=True, blank=True,max_length = 200)

    slug = models.SlugField(max_length = 100)
   
    order = models.IntegerField()

    online = models.BooleanField("Online",default=True)
   
    
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Place'
        
    def __str__(self):
     return self.name

    def place_photo(self):
            
        return mark_safe('<img src="{}" height="100", width="100"/>'.format(self.logo.url))


# Maker Model

class Person(models.Model):
  
   
    INSTANCESOFPERSON = (
      
        ('actor', 'Actor'),
        ('artist', 'Artist'),
        ('author', 'Author'),
        ('composer', 'Composer'),
        ('creator', 'Creator'), 
        ('painter', 'Painter'),
        ('draughtsman','Draughtsman'),
        ('engineer', 'Engineer'),
        ('scientist', 'Scientist'),
        ('sculptor ', 'Sculptor'),   
        ('architect ', 'Architect'),  
        ('polymath ', 'Polymath'), 
        ('colorist ', 'colorist'),       
        
    ) 
    
   
    last_name = models.CharField(max_length=50,editable=True,default=None,unique=True, help_text='<h3>Last name of the Maker:(e.g., Da Vinci )</h3>')
   
    first_name = models.CharField(max_length=50,default=None, blank=True,verbose_name = 'First Name')
   
    gender = models.CharField(max_length=10,default=None,blank=True, null=True)
   
    type = models.CharField(max_length=30,default=None, choices=INSTANCESOFPERSON,blank=True, null=True)
   
    photo = models.ImageField(upload_to='maker_images')
   
    date_of_birth = models.CharField(max_length=80,default=None,blank=True, null=True)
   
    birth_place = models.CharField(max_length=80,default=None,blank=True, null=True)
   
    date_of_death = models.CharField(max_length=30,blank=True)
   
    death_place = models.CharField(max_length=80,default=None,blank=True, null=True)

    online = models.BooleanField("Online",default=True)
   
    same_as = models.URLField(max_length=100,default=None,blank=True, null=True, help_text='<h3>it is the same person as the link (https://en.wikipedia.org/wiki/Leonardo_da_Vinci)</h3>')
    

    order = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Maker'
    def __str__(self):
            return self.last_name
    
       
    def person_photo(self):
            
        return mark_safe('<img src="{}" height="100", width="100"/>'.format(self.photo.url))


