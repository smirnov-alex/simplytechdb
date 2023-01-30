from django.contrib import admin

from .models import PhoneBook, Site, Category, SiteCommon, SiteEquipment, SiteBatteries, \
    SiteRRL, SiteEnergy, SiteOldInfo, Comment, SiteQuazar, DutyShedule, DutyTimetable


class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'status', 'alternative', 'category')
    list_display_links = ('title',)
    search_fields = ('title', 'address', 'alternative')


class SiteCommonAdmin(admin.ModelAdmin):
    list_display = ('title', 'distance', 'priority', 'type_hardware')
    list_display_links = ('title',)
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('author', 'text')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Category)
admin.site.register(SiteCommon, SiteCommonAdmin)
admin.site.register(SiteEquipment)
admin.site.register(SiteBatteries)
admin.site.register(SiteRRL)
admin.site.register(SiteEnergy)
admin.site.register(SiteOldInfo)
admin.site.register(SiteQuazar)
admin.site.register(PhoneBook)
admin.site.register(DutyShedule)
admin.site.register(DutyTimetable)
