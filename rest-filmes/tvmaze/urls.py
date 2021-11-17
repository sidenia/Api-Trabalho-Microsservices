from django.urls import path
# from tvmaze.views import *
from . import views

urlpatterns = [
    path('home/', views.home ,name='home'),
]
