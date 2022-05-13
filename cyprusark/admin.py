from django.contrib import admin

from .models import Slider, Collection, Museum, Museum_Item
# Register your models here.

# Header

admin.site.site_header ='CyprusArk'


# Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','order')


admin.site.register(Slider, SliderAdmin)


# Collection
class CollectionAdmin(admin.ModelAdmin):
    

    list_display = (
        'collection_name', 
        
        )
    list_filter = (
        
        'collection_name',
    
    )
   
admin.site.register(Collection,CollectionAdmin)
# Museum
class MuseumAdmin(admin.ModelAdmin):
    

    list_display = (
        'museum_name', 
        'online', 
        
        )
    list_filter = (
        
        'museum_name',
    
    )
   
admin.site.register(Museum,MuseumAdmin)


#Museum Item
class Museum_ItemAdmin(admin.ModelAdmin):

    
      
    list_display = (
        'admin_photo',
        'title',
        'classification',
        'period',
        'online',
        'order',
       
       
        
        
        )
    list_filter = (
        
        'date',
        'classification',
        'period',
        'collection',
     
    
    )
   
    search_fields = [
        'title',
        'date',
        'period',
       
      
    ]
admin.site.register(Museum_Item,Museum_ItemAdmin)
    





