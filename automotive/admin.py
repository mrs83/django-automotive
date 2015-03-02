from django.contrib import admin

from .models import Brand, Model


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Brand, BrandAdmin)


class ModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'year')
    list_filter = ('brand', 'year')
    search_fields = ('full_name',)

admin.site.register(Model, ModelAdmin)
