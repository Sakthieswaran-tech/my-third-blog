from django.shortcuts import render
from .models import Post
from django.utils import timezone
def poster(request):
    post=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/poster.html',{'posts':post})
# Create your views here.
