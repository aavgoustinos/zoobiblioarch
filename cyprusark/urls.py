from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('<slug:slug>/', views.bundle, name="bundle"),
    path('<slug:slug_bundle>/<slug:slug>/', views.item, name="item"),

   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)