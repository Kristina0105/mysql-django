from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from cities.forms import RestaurantForm, SpecializationForm
from cities.models import Restaurants


def index(request):
    return render(request, 'index.html')

class RestaurantList(ListView):
    model = Restaurants
    paginate_by = 10
    template_name = 'list.html'

def add_r(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RestaurantForm()
    return render(request, 'add_restaurant.html', {'form': form})

def delete_r(request, id):
    restaurant = get_object_or_404(Restaurants, id=id)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('/')
    return render(request, 'confirm_delete_restaurant.html', {'restaurant': restaurant})

def update_r(request, id):
    contact = get_object_or_404(Restaurants, id=id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RestaurantForm(instance=contact)
    return render(request, 'update_restaurant.html', {'form': form})

def search_r(request):
    form = SpecializationForm(request.GET)
    query = request.GET.get('query')
    restaurants = Restaurants.objects.all()

    if query:
        restaurants = restaurants.filter(specialization__icontains=query)

    if form.is_valid() and form.cleaned_data['specialization']:
        restaurants = restaurants.filter(specialization=form.cleaned_data['specialization'])
    return render(request, 'search_restaurant.html', {'restaurants': restaurants, 'query': query, 'form': form})
