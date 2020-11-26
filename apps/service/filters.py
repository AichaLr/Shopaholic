import django_filters
from .models import *


class ServiceFilters(django_filters.FilterSet):
   wilaya = django_filters.ChoiceFilter(choices=service.wilay)

   class Meta:
        Model = service
        fields = ['wilaya']

