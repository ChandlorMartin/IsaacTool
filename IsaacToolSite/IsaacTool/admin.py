from django.contrib import admin

# Register your models here.

from .models.material_model import Material

admin.site.register(Material)