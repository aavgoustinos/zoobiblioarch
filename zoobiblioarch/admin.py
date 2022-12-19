from django.contrib import admin
from zoobiblioarch.models import *

admin.site.site_header ='ZooBi(bli)oArch'

admin.site.register(Author) 
admin.site.register(Region) 

class ArticleAdmin(admin.ModelAdmin):
       
    list_display = ('title','year','DOI','journal',)
    filter_horizontal = ('keyword', 'region',)
    list_filter = ('year','journal',)
    list_editable =('journal',)
    
    
admin.site.register(Article, ArticleAdmin)


class JournalAdmin(admin.ModelAdmin):
       
    list_display = ('journal_title',)

admin.site.register(Journal, JournalAdmin)


class keywordAdmin(admin.ModelAdmin):
       
    list_display = ('keyword',)

admin.site.register(keyword, keywordAdmin)




    
 








