from django.contrib import admin
from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.
admin.site.register(models.Child)
class ChildAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['collection']
    # prepopulated_fields = {
    #     'slug': ['title']
    # }
    # actions = ['clear_inventory']
    # list_display = ['title', 'unit_price',
    #                 'inventory_status', 'collection_title']
    # list_editable = ['unit_price']
    # list_filter = ['collection', 'last_update', InventoryFilter]
    # list_per_page = 10
    # list_select_related = ['collection']
    search_fields = ['first_name']

admin.site.register(models.Parent)
admin.site.register(models.Devices)