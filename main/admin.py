from django.contrib import admin
from .models import Kiosk, IceCream, Parent, Child

admin.site.register(Kiosk)
admin.site.register(IceCream)
admin.site.register(Parent)
admin.site.register(Child)