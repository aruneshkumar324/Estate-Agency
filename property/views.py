from django.shortcuts import render
from .models import Property
from django.core.paginator import Paginator


def property(request):
    # properties = Property.objects.all()
    properties = Property.objects.order_by('-updated_date')

    paginator = Paginator(properties, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)


    data = {
        "properties": page_object,
    }
    return render(request, 'property/properties.html', data)


def property_details(request, id):
    detail = Property.objects.filter(pk=id).get()
    data = {
        "detail": detail,
    }
    return render(request, 'property/property_details.html', data)