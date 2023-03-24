from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Media
from .forms import MediaForm, ContactForm
from django.db.models import Q
# Create your views here.

# Define a view function to display a list of all the instances of your model. You can use the all() method to retrieve all instances of the model:

def home(request):
    media = Media.objects.all()
    return render(request, 'media_app/home.html', {'media': media})


def about(request):

    return render(request,  'media_app/about.html', )


# Define a view function to handle file uploads for your model:

# def create(request):
#     if request.method == 'POST':
#         form = Media(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('File uploaded successfully.')
#     else:
#         form = Media()
#     return render(request, 'create.html', {'form': form})


def model_thumbnail(request, pk):
    media = get_object_or_404(Media, pk=pk)
    image_data = open(media.thumbnail.path, 'rb').read()
    return HttpResponse(image_data, content_type='image/jpeg')

def media_list(request):
    media = Media.objects.all()
    return render(request, 'media_app/media_list.html', {'media': media})


def create(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save()
            return redirect('detail', pk=media.pk)
    else:
        form = MediaForm()
    return render(request, 'media_app/create.html', {'form': form})

def detail(request, pk):
    media = get_object_or_404(Media, pk=pk)
    return render(request, 'media_app/detail.html', {'media': media})

def view_video(request,pk):
    media = get_object_or_404(Media, pk=pk)
    return render(request, 'media_app/view_video.html', {'media': media})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            pass
    else:
        form = ContactForm()
    return render(request, 'media_app/contact.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        media = Media.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        media = Media.objects.all()
    return render(request, 'media_app/detail.html', {'media': media, 'query': query})