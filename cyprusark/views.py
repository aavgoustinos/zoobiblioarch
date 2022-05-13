from django.shortcuts import render
from .models import Museum_Item, Slider, Collection, Museum

# HomePage collections view
def homepage(request):
    slider = Slider.objects.all().order_by("order").filter(online=True)
    collection = Collection.objects.all().order_by("order").filter(online=True)
    museum = Museum.objects.all().filter(online=True)
    context = {'slider': slider,'collection':collection,'museum':museum}
    return render(request, 'core/homepage.html', context)


# The Collection Page
def collection(request,slug):
    collection = Collection.objects.filter(online=True).get(slug=slug)
    items = collection.museum_item_set.all().order_by("order").filter(online=True)
    context = {'collection':collection,'items':items}
    return render(request, 'core/collection.html', context)

