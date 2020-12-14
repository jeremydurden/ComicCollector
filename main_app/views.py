from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from .models import Comic

class ComicCreate(CreateView):
    model = Comic
    fields = '__all__'

class ComicUpdate(UpdateView):
    model = Comic
    fields = ['issue', 'writer', 'artist', 'description']

class ComicDelete (DeleteView):
    model = Comic
    success_url = '/comics/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    comics = Comic.objects.all()
    return render(request, 'comics/index.html', { 'comics': comics })

def comics_detail(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    return render(request, 'comics/detail.html', { 'comic': comic })

