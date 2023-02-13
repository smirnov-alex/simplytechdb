from django.urls import path, include

from .views import index, by_category, phonebook, site_view, new_site, SearchResultsView, bss_info, tn_info, shedule, \
    useful_sites, new_site_info

urlpatterns = [
    path('tn_info/', tn_info, name='tn_info'),
    path('bss_info/', bss_info, name='bss_info'),
    path('phonebook/', phonebook, name='phonebook'),
    path('useful_sites/', useful_sites, name='useful_sites'),
    path('shedule/', shedule, name='shedule'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path("site/<int:site_id>/", site_view, name="site_view"),
    path('new_info/', new_site_info, name='new_site_info'),
    path('new/', new_site, name='new'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
]
