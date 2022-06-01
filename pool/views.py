from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Image,Follower
from pool.forms import ImageForm
from .email import send_email



# Create your views here.
@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('galleries')
    else:
        form = ImageForm()

    return render(request,'new_article.html',{"form":form})

def galleries(request):
    galleries = Image.galleries()

    if request.method == 'POST':
        form = FollowerForm(request.POST)
        if form.is_valid():
            print('valid!')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            follower = Follower(name=name,email=email)
            follower.save()

            send_email(name,email)

        HttpResponseRedirect('galleries')
    else:
        form = FollowerForm()

    return render(request,'galleries/index.html',{"galleries":galleries})


@login_required(login_url='/accounts/login')
def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)

    except DoesNotExist:
        raise Http404()

    return render(request,'galleries/image.html',{"image":image,"followerForm":form})


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

