from .models import *
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')
# fields = ('title', 'description', 'create')
