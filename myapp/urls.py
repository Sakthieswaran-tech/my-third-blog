from django.urls import path
from . import views
urlpatterns = [
    path('',views.poster,name='poster.html')]