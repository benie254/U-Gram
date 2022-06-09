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
    url(r'^accounts/profile/(\d+)/$', views.user_images,name='userImages'),
    # url(r'^user/(\d+)/$',views.user_images,name='userImages'),
    path('add/image',views.new_image,name='newImage'),
    url(r'^gallery/feed/(\d+)/$',views.user_feed,name='feed'),
    path('search/term/',views.search_results,name='search_results'),
    url(r'^profile/(\d+)/bio/add/$',views.user_bio,name='bio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)