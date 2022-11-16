from django.urls import path
from django.urls import include

from .views import show_index_page, show_category, show_about_us, show_contacts
from .views import send_contact_form, send_form_success, send_form_error

urlpatterns = [

    path('', show_index_page, name="show_index_page"),
    path('about/', 	show_about_us, name='show_about_us'),
    path('contacts/', 	show_contacts, name='show_contacts'),
    path('category/<str:cpu_slug>/', 	show_category, name='show_category'),

    path('send-contact-form/', send_contact_form, name='send_contact_form'),
    path('send-form-success/', send_form_success, name='send_form_success'),
	path('send-form-error/', send_form_error, name='send_form_error'),

]