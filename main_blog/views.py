from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'jamini',
#         'title': 'blog post 1',
#         'content': 'first post content',
#         'date': 'april 3,2023'
#     },
#      {
#         'author': 'karim',
#         'title': 'blog post 2',
#         'content': 'first post content',
#         'date': 'april 4,2023'
#     }
# ] 

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'main_blog/home.html',context)

def about(request):
    return render(request,'main_blog/about.html',{'title':'About'})