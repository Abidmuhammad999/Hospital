from django.urls import path,include
from .import views
urlpatterns = [
   path('',views.index,name='Home'),
   path('about',views.about,name='About'),
   path('booking',views.booking,name='Booking'),
   path('doctors',views.doctors,name='Doctros'),
   path('contact',views.contact,name='Contact'),
   path('department',views.department,name='Departments'),

]