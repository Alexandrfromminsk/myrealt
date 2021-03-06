import random
from django import forms
from .models import Marks, Criteria

class MarkForm(forms.Form):

    def __init__(self, fields, *args, **kwargs):
        super(MarkForm, self).__init__(*args, **kwargs)
        for field in fields:
            self.fields['{}'.format(field)] = forms.IntegerField(required=True, initial=random.randrange(10))

    name_field = forms.CharField(required=True)
    link_field = forms.CharField(required=True)
    is_ready = forms.BooleanField(required=False, initial=False)

