from django.forms import ModelForm

from .models import Site, Comment, SiteCommon, SiteBatteries


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ('title', 'address', 'status', 'alternative', 'category')


class SiteCommonForm(ModelForm):
    class Meta:
        model = SiteCommon
        fields = ('title', 'distance', 'priority', 'type_hardware')


class SiteAkbForm(ModelForm):
    class Meta:
        model = SiteBatteries
        fields = ('title', 'system_of_voltage', 'num_of_rect', 'battery_type', 'battery_num', 'battery_cap',
                  'battery_date')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
