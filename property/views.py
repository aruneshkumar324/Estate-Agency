from django.shortcuts import render
from .models import Property


def property(request):
    # properties = Property.objects.all()
    properties = Property.objects.order_by('-updated_date')
    data = {
        "properties": properties
    }
    return render(request, 'property/properties.html', data)


def property_details(request, id):
    detail = Property.objects.filter(pk=id).get()
    data = {
        "detail": detail,
    }
    return render(request, 'property/property_details.html', data)