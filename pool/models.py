from django.db import models
import datetime as dt
from location_field.models.plain import PlainLocationField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
# class Editor(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#     phone = models.CharField(max_length=10,blank=True)
#     profile_pic = CloudinaryField('image')
#
#     def __str__(self):
#         return self.first_name
#
#     def save_editor(self):
#         self.save()
#
#     class Meta:
#         ordering = ['first_name']



class tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tag(self):
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter(category=self).delete()

    def update_category(self):
        Category.objects.filter(category=self).update(category=self.category)


class Location(models.Model):
    city = models.CharField(max_length=255,null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7,null=True)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        Location.objects.filter(location=self).delete()

    def update_location(self):
        Location.objects.filter(location=self).update(location=self.location)

class PPhoto(models.Model):
    p_pic = CloudinaryField('image', null=True)
    editor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

class Follower(models.Model):
    follower = models.CharField(max_length=30)

    def __str__(self):
        return self.follower

    def save_follower(self):
        self.save()

class Comment(models.Model):
    comment = HTMLField()

class Image(models.Model):
    pic = CloudinaryField('image')
    title = models.CharField(max_length=60,null=True)
    description = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    tag = models.ManyToManyField(tag)
    follower = models.ManyToManyField(Follower,null=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    published = models.DateTimeField(auto_now_add=True)
    comment = models.ManyToManyField(Comment,null=True)
    like = models.ManyToManyField(User, blank=True, related_name="votes")

    @classmethod
    def galleries(cls):
        gallery = cls.objects.all()

        return gallery


    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(published__date=today)

        return gallery

    @classmethod
    def days_gallery(cls,date):
        gallery = cls.objects.filter(published__date=date)

        return gallery


    @classmethod
    def search_by_tag(cls, tag_term):
        gallery = cls.objects.filter(tag__name=tag_term)

        return gallery


    @classmethod
    def search_by_category(cls, category_term):
        gallery = cls.objects.filter(category__category=category_term)
        return gallery

    @classmethod
    def search_by_term(cls, search_term):
        gallery = cls.objects.filter(description__icontains=search_term)
        return gallery

    @classmethod
    def search_by_location(cls, location_term):
        gallery = cls.objects.filter(location__location=location_term)
        return gallery

    @classmethod
    def get_by_id(cls, id):
        gallery = cls.objects.filter(id=id)
        return gallery

    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter(id=self).delete()

    def update_image(self):
        updated_image = Image.objects.filter(pic=self.id).update(pic=self.pic,title=self.title,description=self.description,editor=self.editor,category=self.category,location=self.location)



