from django.contrib import admin
from django.apps import apps
from .models import Produk, Kategori, Status

# Register your models here.
admin.site.register(Produk)
admin.site.register(Kategori)
admin.site.register(Status)
