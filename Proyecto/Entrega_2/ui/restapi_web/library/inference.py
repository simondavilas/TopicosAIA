from django import forms
from library.models import InferenceModel

class Inference(forms.ModelForm):

    class Meta:
        model = InferenceModel
        fields = ['elevation', 'slope', 'horizontal_distance_to_hidrology', 'vertical_distance_to_hidrology', 'horizontal_distance_to_roadways', 'hillshade_9_am',
                'hillshade_noon', 'horizontal_distance_to_firepoints', 'wilderness_area']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['elevation', 'slope', 'horizontal_distance_to_hidrology', 'vertical_distance_to_hidrology', 'horizontal_distance_to_roadways', 'hillshade_9_am',
                'hillshade_noon', 'horizontal_distance_to_firepoints', 'wilderness_area'].widget.attrs.update({
            'class': 'form-control',
        })