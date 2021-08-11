from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Site, Category
from .forms import SiteForm


def index(request):
    sites = Site.objects.all()
    categories = Category.objects.all()
    return render(request, 'techdb/index.html', {'sites': sites, 'categories': categories,})

def by_category(request, category_id):
    sites = Site.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'sites': sites, 'categories': categories, 'current_category': current_category}
    return render(request, 'techdb/by_category.html', context)

def site_view(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    return render(request, "techdb/site.html", {'site': site})

class SiteCreateView(CreateView):
    template_name = 'techdb/new.html'
    form_class = SiteForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

