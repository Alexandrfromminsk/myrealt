from django import forms
from .models import Marks

class MarkForm(forms.Form):
    name_field = forms.CharField(required=True)

    class Meta:

        model = Marks
        fields = ('pseudonim','value', 'weight',)
