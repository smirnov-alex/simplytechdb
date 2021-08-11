from django.forms import ModelForm

from .models import Site

class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ('title', 'address', 'status', 'alternative', 'category')