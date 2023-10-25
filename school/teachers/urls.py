from django.urls import path
from . import views
urlpatterns = [
    path('', views.home1, name='home1.html'),
    path('contact',views.contact, name='contact.html'),
    path('classes', views.classes, name='class.html'),
    path('teachers', views.teachers, name='teachers.html')
]
