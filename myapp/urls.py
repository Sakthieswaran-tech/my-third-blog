from django.urls import path
from . import views
urlpatterns = [
    path('',views.poster,name='poster.html'),path('post/<int:pk>/',views.post_details,name="post_details")]