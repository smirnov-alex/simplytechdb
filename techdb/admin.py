from django.contrib import admin

from .models import Site, Category


class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'status', 'alternative', 'category')
    list_display_links = ('title',)
    search_fields = ('title', 'address', 'alternative')

admin.site.register(Site, SiteAdmin)
admin.site.register(Category)
