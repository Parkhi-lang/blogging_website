from django.shortcuts import redirect, get_object_or_404, render
from .models import *

# Create your views here.
def posts_by_category(request,category_id):
    print(category_id)
    #fetch the posts that belongs to the category with the given id
    posts = Blog.objects.filter(status = 'Published',category = category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context ={
        'posts': posts,
        'category': category,
    }
    return render(request,'posts_by_category.html',context)
