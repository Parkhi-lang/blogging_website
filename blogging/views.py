
from django.shortcuts import render
from blogs.models import Category,Blog
from assignments.models import *

def home(request):
    
    featured_posts = Blog.objects.filter(is_featured = True,status = 'Published').order_by('updated_at')
    print(featured_posts)
    posts = Blog.objects.filter(is_featured = False,status='Published')
    print(posts)
    try:
        about = About.objects.get()
    except:
        about = None

    context ={
        
        'featured_posts':featured_posts,
        'posts': posts,
        'about':about,
    }
    #change in home.html
    return render(request,'home.html', context)