from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-created_date')
    data = {
        "blogs": blogs
    }
    return render(request, 'blog/blog.html', data)


def blog_details(request, id):
    blog = Blog.objects.filter(pk=id).get()
    data = {"blog": blog}
    return render(request, 'blog/blog_details.html', data)