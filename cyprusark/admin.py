from django.contrib import admin
from .models import  CreativeWork,  Bundle, Slider, Place, Person


admin.site.index_title  =  "Admin Area"
# Slider

class SliderAdmin(admin.ModelAdmin):
   
    list_display = ('slider_photo','title','order')


admin.site.register(Slider, SliderAdmin)


# Collection
class BundleAdmin(admin.ModelAdmin):
    

    list_display = (
        'bundle_photo',
        'name', 
        'order',
        'online',
        
        )
    
    list_editable = (
        
        'online',
        'order',
    
    
    )
   
admin.site.register(Bundle,BundleAdmin)
# Museum
class PlaceAdmin(admin.ModelAdmin):
    

    list_display = (
        'place_photo', 
        'name', 
        'classification',
        'order',
        'online', 
  
        
        )
    list_editable = (
        
        'online',
        'classification',
        'order',
    
    
    )

   
admin.site.register(Place,PlaceAdmin)


#Museum Item
class CreativeWorkAdmin(admin.ModelAdmin):

    list_display = (

        'creative_photo',
        'title',
        #'classification',
        'date',
        'period',
        'maker',
        'online',
        'order',
        
        )
    list_filter = (
        
        'date',
       # 'classification',
        'period',
    
     
    
    )
    list_editable = (
        
        'online',
       # 'classification',
        'order',
    )
    list_per_page =10
    
   
    search_fields = [
        'title',
        'date',
        'period',
       
      
    ]
admin.site.register(CreativeWork,CreativeWorkAdmin)
    
# Maker

class PersonAdmin(admin.ModelAdmin):
    

    list_display = (
        'person_photo',
        'last_name',
        'first_name', 
        'type', 
        'gender',
        'date_of_birth',
        'birth_place',
        'date_of_death',
        'death_place',
        'same_as',
        'order',
        'online',
        
        )
    list_editable = (
        
        'online',
        'order',
        'type',
    
    
    )
    list_per_page =10
   
admin.site.register(Person,PersonAdmin)

