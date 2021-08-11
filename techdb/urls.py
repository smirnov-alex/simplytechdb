from django.urls import path

from .views import index, by_category, SiteCreateView, site_view

urlpatterns = [
    path("site/<int:site_id>/", site_view, name="site_view"),
    path('new/', SiteCreateView.as_view(), name='new'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
]
