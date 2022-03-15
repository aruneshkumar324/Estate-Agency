from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator


# Create your views here.
def blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-created_date')

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    data = {
        "blogs": page_object
    }
    
    return render(request, 'blog/blog.html', data)


def blog_details(request, id):
    blog = Blog.objects.filter(pk=id).get()
    data = {"blog": blog}
    return render(request, 'blog/blog_details.html', data)