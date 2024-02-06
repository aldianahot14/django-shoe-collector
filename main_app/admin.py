# Register your models here.
from django.contrib import admin
from .models import Shoe, Cleaning, ShoeAccessory

admin.site.register(Shoe)
admin.site.register(Cleaning)
admin.site.register(ShoeAccessory)
