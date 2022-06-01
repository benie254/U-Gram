from django.contrib import admin
from .models import Image,tag,Category,Location


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)


# Register your models here.
admin.site.register(Image,ImageAdmin)
admin.site.register(tag)
admin.site.register(Category)
admin.site.register(Location)
