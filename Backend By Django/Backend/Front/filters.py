from django_filters.rest_framework import FilterSet
from .models import Child

class ChildFilter(FilterSet):
  class Meta:
    model = Child
    fields = {
      'id': ['exact'],
    }