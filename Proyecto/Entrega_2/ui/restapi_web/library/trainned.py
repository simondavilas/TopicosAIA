from django import forms
from library.models import TrainSet

class Trainned(forms.ModelForm):

    class Meta:
        model = TrainSet
        fields = ['modelos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['modelos'].widget.attrs.update({
            'class': 'form-control',
        })