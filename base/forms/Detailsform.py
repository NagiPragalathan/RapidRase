from django import forms
from base.models import Details, DetailsImage

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['description', 'points']

class ImageForm(forms.ModelForm):
    class Meta:
        model = DetailsImage
        fields = ['image']
