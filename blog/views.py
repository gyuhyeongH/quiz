from django.shortcuts import render, redirect
from .models import Category,Article

# Create your views here.

def category(request):
    if request.method == 'GET':
        all_category = Category.objects.all()
        return render(request, 'index.html', {'category': all_category})



def write(request):
    if request.method == 'GET':
        all_category = Category.objects.all()
        return render(request, 'new.html', {'category': all_category})

    elif request.method == 'POST':
        Article.title = request.POST.get('my-title', '')
        Article.content = request.POST.get('my-content', '')
        Article.category = request.POST.get('my-cate', '')
        Article.save()
        return redirect('/index')