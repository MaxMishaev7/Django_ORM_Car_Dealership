from django.contrib import admin

# Register your models here.
from .models import Car, Client, Sale
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Sale)

