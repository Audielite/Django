from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create function to add to a list
def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})
#create function for places visited to return results
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})
#function to catch errors
def places_is_visited(request):
    if request.method == 'POST':
        pk= request.POST.get('pk')
        place = get_object_or_404(pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')
