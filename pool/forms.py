from django import forms
from .models import Image,Follower,Profile,Comment
from cloudinary.models import CloudinaryField


class FollowerForm(forms.Form):
    pass

class ImageForm(forms.ModelForm):

    # pic = CloudinaryField('image')
    # description = forms.EmailField(label='Email')
    class Meta:
        model = Image
        exclude = ['editor','pub_date','tag','category','title','location','follower','like','comment']

class ProfilePhotoForm(forms.ModelForm):

    # pic = CloudinaryField('image')
    # description = forms.EmailField(label='Email')
    class Meta:
        model = Profile
        exclude = ['editor','bio']

class BioForm(forms.ModelForm):

    # pic = CloudinaryField('image')
    # description = forms.EmailField(label='Email')
    class Meta:
        model = Profile
        exclude = ['editor','p_pic']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['comment']