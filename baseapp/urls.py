from django.urls import path
from django.urls import include

from .views import show_index_page, show_category, show_about_us, show_contacts

urlpatterns = [

    path('', show_index_page, name="show_index_page"),
    path('about/', 	show_about_us, name='show_about_us'),
    path('contacts/', 	show_contacts, name='show_contacts'),
    path('category/<str:cpu_slug>/', 	show_category, name='show_category'),

]