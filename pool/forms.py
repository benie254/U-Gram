from django import forms
from .models import Image,Follower,PPhoto,Comment
from cloudinary.models import CloudinaryField


class FollowerForm(forms.Form):
    pass

class ImageForm(forms.ModelForm):

    # pic = CloudinaryField('image')
    # description = forms.EmailField(label='Email')
    class Meta:
        model = Image
        exclude = ['editor','pub_date','tag','category','title','location','follower']

class ProfilePhotoForm(forms.ModelForm):

    # pic = CloudinaryField('image')
    # description = forms.EmailField(label='Email')
    class Meta:
        model = PPhoto
        exclude = ['editor']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['comment']