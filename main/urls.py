from django.urls import path
from .views import home, about, courses

urlpatterns = [
path('courses/',courses,name='courses-url'),
path('about/',about,name='about-url'),
path('',home,name='home-url')

]
