from django.shortcuts import render
from .models import Agent
from blogs.models import Blog
from property.models import Property
from django.core.paginator import Paginator



# Create your views here.
def home(request):

    agents = Agent.objects.all()[:3]
    blogs = Blog.objects.all()[:4]
    properties = Property.objects.all()[:4]
    
    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "agents": agents,
        "blogs": blogs,
        "properties": properties,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    return render(request, 'pages/home.html', data)


def about(request):
    teams = Agent.objects.all()[:3]

    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "teams": teams,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
        }

    return render(request, 'pages/about.html', data)


def contact(request):
    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    return render(request, 'pages/contact.html', data)


def agents(request):
    agents = Agent.objects.all()

    paginator = Paginator(agents, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "agents": page_object,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    return render(request, 'pages/agents.html', data)


def agent_profile(request, id):
    agent = Agent.objects.filter(pk=id).get()
    properties = Property.objects.order_by('-created_date')

    data = {"agent": agent, "properties": properties}
    return render(request, 'pages/agent_profile.html', data)