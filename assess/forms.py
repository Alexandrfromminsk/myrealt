from django import forms
from .models import Marks, Criteria

class MarkForm(forms.Form):

    def __init__(self, fields, *args, **kwargs):
        super(MarkForm, self).__init__(*args, **kwargs)
        for field in fields:
            self.fields['{}'.format(field)] = forms.IntegerField(required=True, initial=0)

    name_field = forms.CharField(required=True)
    link_field = forms.CharField(required=True)
    is_ready = forms.BooleanField(required=False, initial=False)

    #
    # for i in range(number_of_fields):
    #     fieldname = 'mark{}'.format(i)
    #     fieldname = forms.IntegerField(required=True, initial=0)

    # class Meta:
    #
    #     model = Marks
    #     fields = ('pseudonim','value', 'weight',)
