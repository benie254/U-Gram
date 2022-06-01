from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image
from pool.forms import
from django.contrib.auth import login, authenticate


# Create your views here.
def galleries(request):
    galleries = Image.galleries()

    return render(request,'galleries/index.html',{"galleries":galleries})


def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)

    except DoesNotExist:
        raise Http404()

    return render(request,'galleries/image.html',{"image":image})


def tag_results(request):

    if 'image' in request.GET and request.GET["image"]:
        tag_term = request.GET.get("image")
        searched_images = Image.search_by_tag(tag_term)

        message = f"{tag_term}"

        return render(request,'galleries/search_results.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search_results.html',{"message":message})


def category_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category_term = request.GET.get("image")
        searched_images = Image.search_by_category(category_term)

        message = f"{category_term}"

        return render(request,'galleries/search_results.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search_results.html',{"message":message})


def location_results(request):

    if 'image' in request.GET and request.GET["image"]:
        location_term = request.GET.get("image")
        searched_images = Image.search_by_location(location_term)

        message = f"{location_term}"

        return render(request,'galleries/search_results.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search_results.html',{"message":message})

