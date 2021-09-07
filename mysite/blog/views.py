from django.shortcuts import render

from .models import Post

def frontpage(request):

    
    return render(request, 'blog/frontpage.html')
