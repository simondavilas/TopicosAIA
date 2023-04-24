from django import forms
from library.models import DataSet

class Processed(forms.ModelForm):

    class Meta:
        model = DataSet
        fields = ['conjunto_de_datos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['conjunto_de_datos'].widget.attrs.update({
            'class': 'form-control',
        })