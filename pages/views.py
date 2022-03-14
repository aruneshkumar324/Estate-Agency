from django.shortcuts import render
from .models import Agent
from blogs.models import Blog
from property.models import Property


# Create your views here.
def home(request):

    agents = Agent.objects.all()[:3]
    blogs = Blog.objects.all()[:4]
    properties = Property.objects.all()[:4]

    print(agents)
    data = {
        "agents": agents,
        "blogs": blogs,
        "properties": properties,
    }

    return render(request, 'pages/home.html', data)


def about(request):
    teams = Agent.objects.all()[:3]
    return render(request, 'pages/about.html', {"teams": teams})


def contact(request):
    return render(request, 'pages/contact.html')


def agents(request):
    agents = Agent.objects.all()
    return render(request, 'pages/agents.html', {"agents": agents})


def agent_profile(request, id):
    agent = Agent.objects.filter(pk=id).get()
    data = {"agent": agent}
    return render(request, 'pages/agent_profile.html', data)