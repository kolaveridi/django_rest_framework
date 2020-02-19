from django.contrib import admin

# Register your models here.
from .models import (
    LocationData,
    Region,
    State,
    City,
    Country
)


admin.site.register(LocationData)
admin.site.register(Region)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Country)