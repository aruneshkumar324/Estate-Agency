from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
from property.models import Property


# Create your views here.
def blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-created_date')

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "blogs": page_object,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    
    return render(request, 'blog/blog.html', data)


def blog_details(request, id):
    blog = Blog.objects.filter(pk=id).get()

    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "blog": blog,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    return render(request, 'blog/blog_details.html', data)