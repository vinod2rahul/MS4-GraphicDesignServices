from django.contrib import admin
from .models import Design, Order

admin.site.site_header = "Graphic Design"
admin.site.site_title = "Graphic Design"

# Register your models here.
admin.site.register(Design)
admin.site.register(Order)
