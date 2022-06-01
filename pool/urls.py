from django.urls import path,re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.galleries,name='galleries'),
    path('search/tag/',views.tag_results,name='tag_results'),
    path('search/category/',views.category_results,name='category_results'),
    path('search/location/',views.location_results,name='location_results'),
    url(r'^image/(\d+)/$',views.image,name='image'),
    path('gallery/image',views.new_image,name='newImage')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)