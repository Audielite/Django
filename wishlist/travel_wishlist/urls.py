from django.conf.urls import url
from . import views
#URLs for desired pages/sections
urlpatterns = [
url(r'^$', views.place_list, name='place_list'),
url(r'^visited$', views.places_visited, name='places_visited'),
url(r'^isvisited$', views.places_is_visited, name='places_is_visited'),
]
