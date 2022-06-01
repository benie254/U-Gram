from django import forms
from .models import Image,Follower


class FollowerForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor','pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
