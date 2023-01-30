from django.forms import ModelForm

from .models import Site, Comment


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ('title', 'address', 'status', 'alternative', 'category')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
