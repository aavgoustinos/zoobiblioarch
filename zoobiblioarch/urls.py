from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('team', views.team, name="team"),
    path('about', views.about, name="about"),
    path('articles', views.list_articles, name="list_articles"),
    path('json', views.json, name="json"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)