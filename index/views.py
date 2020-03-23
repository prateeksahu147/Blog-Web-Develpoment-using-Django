from django.shortcuts import render,  get_object_or_404
from .models import TopPosts, Projects
def index(request):
    Top_posts=TopPosts.objects
    posts = Projects.objects
    return render(request, 'index/index.html', {'Top_posts':Top_posts, 'posts': posts})

def projects(request):
    posts= Projects.objects
    return render(request, 'index/projects.html', {'posts': posts})

def detail(request, blog_id ):
    posts= Projects.objects
    details = get_object_or_404(Projects, pk=blog_id)
    return render(request, 'index/projectDetail.html',{'posts': posts, 'blog': details})