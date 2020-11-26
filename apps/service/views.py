from django.core.paginator import InvalidPage
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.utils.http import urlquote
from django.views import generic
from django.utils import timezone
from .models import service,category

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, ListView, View, TemplateView

from .signals import review_added
from oscar.core.loading import get_classes, get_model
from oscar.core.utils import redirect_to_referrer
from .filters import *
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'service/index.html'
    context_object_name = 'service_tt'

    def get_queryset(self):
        return service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServiceFilters(self.request.GET, queryset=service.objects.all())
        context['categories'] = category.objects.all()
        return context


class CategoriesView(generic.ListView):
    template_name = 'service/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return category.objects.all()



class CategoryView(generic.DetailView):
    model = category
    template_name = 'service/category.html'

class ServiceView(generic.DetailView):
    model = service
    template_name = 'service/detail.html'


