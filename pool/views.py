from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Image,Follower,PPhoto
from pool.forms import ImageForm,FollowerForm,ProfilePhotoForm,CommentForm
from .email import send_email

from django.template import RequestContext




# Create your views here.
@login_required(login_url='/accounts/login/')
def new_image(request):

    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid!')
            pic = form.cleaned_data['pic']
            description = form.cleaned_data['description']
            image = Image(pic=pic, description=description)
            # image = form.save(commit=True)
            image.editor = current_user
            image.save()
        return redirect('galleries')
    else:
        form = ImageForm()

    return render(request,'user/upload.html',{"form":form})

def galleries(request):
    galleries = Image.galleries()

    current_user = request.user

    if request.method == 'POST':
        folform = FollowerForm(request.POST)
        if folform.is_valid():
            print('valid!')
            follower = Follower(follower=current_user)
            follower.save()
        # HttpResponseRedirect('newsToday')
    else:
        folform = FollowerForm()

    # if request.method == 'POST':
    #     form = FollowerForm(request.POST)
    #     if form.is_valid():
    #         print('valid!')
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         follower = Follower(name=name,email=email)
    #         follower.save()
    #
    #         send_email(name,email)
    #
    #     HttpResponseRedirect('galleries')
    # else:
    #     form = FollowerForm()



    return render(request,'galleries/index.html',{"galleries":galleries,"folform":folform})

def recommend(request,user_id):
    current_user = request.user
    pphoto = PPhoto.objects.filter(editor_id=user_id).last()

    if request.method == 'POST':
        folform = FollowerForm(request.POST)
        if folform.is_valid():
            print('valid!')
            follower = Follower(follower=current_user)
            follower.save()
        HttpResponseRedirect('feed',user_id)
    else:
        folform = FollowerForm()

    if request.method == 'POST':

        cform = CommentForm(request.POST)
        if cform.is_valid():
            print('valid!')
            comment = cform.cleaned_data['comment']
            image = Image(comment=comment)
            # image = form.save(commit=True)
            image.comment = current_user
            image.save()
        return redirect('galleries')
    else:
        cform = ImageForm()

    return render(request, 'galleries/featured.html', {"galleries": galleries, "folform": folform,"cform":cform,"pphoto":pphoto})


@login_required(login_url='/accounts/login')
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

@login_required(login_url='/accounts/login')
def user_images(request,user_id):

    # editor_id = current_user
    images = Image.objects.filter(editor_id=user_id)

    pphoto = PPhoto.objects.filter(editor_id=user_id).last()

    current_user = request.user
    if request.method == 'POST':
        pform = ProfilePhotoForm(request.POST, request.FILES)
        if pform.is_valid():
            print('valid!')
            p_pic = pform.cleaned_data['p_pic']
            p_photo = PPhoto(p_pic=p_pic)
            p_photo.editor = current_user
            p_photo.save()
        return redirect('userImages',user_id)
    else:
        pform = ProfilePhotoForm()

    return render(request,'user/profile.html',{"images":images,"pform":pform,"pphoto":pphoto})


@login_required(login_url='/accounts/login')
def user_feed(request,follower_id):
    galleries = Image.objects.all().order_by('-pic').values()

    # editor_id = current_user
    images = Image.objects.filter(follower=follower_id)

    return render(request, 'galleries/feed.html', {"galleries": galleries})




# def image_post(request, id):
#     if request.method == "POST":
#         instance = Image.objects.get(id=id)
#         if not instance.like.filter(id=request.user.id).exists():
#             instance.like.add(request.user)
#             instance.save()
#
#             return render(request, 'galleries/image.html', context={'image': instance})
#         else:
#             instance.like.remove(request.user)
#             instance.save()
#
#             return render(request, 'galleries/image.html', context={'image': instance})
#
#     return render(request, 'galleries/image.html')

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_term(search_term)

        message = f"{search_term}"

        return render(request,'galleries/search_results.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search_results.html',{"message":message})
