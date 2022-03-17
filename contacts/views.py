from django.shortcuts import render, redirect
from .models import Inquiry
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        interested = request.POST['interested']
        car_title = request.POST['car_title']
        message = request.POST['message']

        print(user_id, car_id, name)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquiry = Inquiry.objects.filter(user_id=user_id, car_id=car_id)
            if has_inquiry:
                return redirect('/property/property_details/'+car_id)
        
        data = Inquiry(name=name, email=email, phone=phone, interested=interested, car_title=car_title, message=message, user_id=user_id, car_id=car_id)

        data.save()

        return redirect('/property/property_details/'+car_id)