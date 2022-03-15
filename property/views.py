from django.shortcuts import render
from .models import Property
from django.core.paginator import Paginator


def property(request):
    # properties = Property.objects.all()
    properties = Property.objects.order_by('-updated_date')

    paginator = Paginator(properties, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "properties": page_object,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    return render(request, 'property/properties.html', data)


def property_details(request, id):
    detail = Property.objects.filter(pk=id).get()

    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()

    data = {
        "detail": detail,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    return render(request, 'property/property_details.html', data)


def search(request):
    properties = Property.objects.order_by('-created_date')

    property_type_field = Property.objects.values_list('property_type', flat=True).distinct()
    city_fields = Property.objects.values_list('city', flat=True).distinct()
    bedroom_fields = Property.objects.values_list('beds', flat=True).distinct()
    bathroom_fields = Property.objects.values_list('baths', flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            properties = properties.filter(title__icontains=keyword)
    

    if 'property_type' in request.GET:
        property_type = request.GET['property_type']
        if property_type:
            properties = properties.filter(property_type__iexact=property_type)
    

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            properties = properties.filter(city__iexact=city)
    

    if 'beds' in request.GET:
        beds = request.GET['beds']
        if beds:
            properties = properties.filter(beds__iexact=beds)

    if 'baths' in request.GET:
        baths = request.GET['baths']
        if baths:
            properties = properties.filter(baths__iexact=baths)



    data = {
        "properties": properties,
        "property_type_field": property_type_field,
        "city_fields": city_fields,
        "bedroom_fields": bedroom_fields,
        "bathroom_fields": bathroom_fields,
    }

    return render(request, 'property/search_query.html', data)