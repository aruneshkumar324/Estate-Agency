from django.db import models
from ckeditor.fields import RichTextField
from .unique_id import generate_unique_id
from multiselectfield import MultiSelectField


class Property(models.Model):
    state_choice = (
        ('AN', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CT', 'Chhattisgarh'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('LD', 'Lakshadweep'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PY', 'Puducherry'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UT', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    )

    property_status = (
        ("Sale", "Sale"),
        ("Sold", "Sold"),
        ("Rent", "Rent"),
    )

    property_type = (
        ("House", "House"),
        ("Villa", "Villa"),
        ("Apartment", 'Apartment'),
    )

    amenities_list = (
        ("Balcony", "Balcony"),
        ("Deck", "Deck"),
        ("Outdoor Kitchen", "Outdoor Kitchen"),
        ("Tennis Courts", "Tennis Courts"),
        ("Parking", "Parking"),
        ("Sun Room", "Sun Room"),
        ("Cable Tv", "Cable Tv"),
        ("Internet", "Internet"),
        ("Concrete Flooring", "Concrete Flooring"),
    )

    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='properties/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='properties/%Y/%m/%d/')
    price = models.IntegerField()
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    state = models.CharField(choices=state_choice, max_length=2)
    city = models.CharField(max_length=200)
    property_id = models.CharField(default=generate_unique_id(), blank=True, max_length=50) # check if u get erorr
    status = models.CharField(choices=property_status, max_length=50)
    property_type = models.CharField(choices=property_type, max_length=50)
    area = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    amenities = MultiSelectField(choices=amenities_list)