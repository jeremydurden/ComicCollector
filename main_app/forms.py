from django.forms import ModelForm
from .models import Cover

class CoverForm(ModelForm):
  class Meta:
    model = Cover
    fields = ['image', 'artist']