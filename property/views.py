from django.shortcuts import render


def property(request):
    return render(request, 'property/properties.html')


def property_details(request):
    return render(request, 'property/property_details.html')