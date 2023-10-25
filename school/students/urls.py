from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('Contact', views.Contact, name='Contact'),
    path('Classes', views.Classes, name='Classes'),
    path('Students', views.Students, name='Students')

]