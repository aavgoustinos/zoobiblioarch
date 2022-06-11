from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import  Bundle, Person, CreativeWork, Slider, Place




# HomePage
def homepage(request):
    slider = Slider.objects.all().order_by("order").filter(online=True)
    bundle = Bundle.objects.all().order_by("order").filter(online=True)
    place = Place.objects.all().filter(online=True)[:1]
    context = {'slider': slider,'bundle':bundle,'place':place}
    return render(request, 'core/homepage.html', context)


# The bundle Page
def bundle(request,slug):
    bundle = Bundle.objects.filter(online=True).get(slug=slug)
    place = Place.objects.all().filter(online=True)[:1]
    items = bundle.creativework_set.all().order_by("order").filter(online=True)
    items_count = bundle.creativework_set.all()
    context = {'bundle':bundle,'items':items,'place':place,'items_count':items_count.count()}
    return render(request, 'core/collection.html', context)



# Creative Work

def item(request,slug_bundle,slug):

    item = CreativeWork.objects.filter(online=True).get(bundle__slug=slug_bundle,slug=slug)
    context ={'item':item,'bundle':bundle}
    return render(request, 'core/item.html',context)




    

