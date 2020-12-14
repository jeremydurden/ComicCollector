from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from .models import Comic
from .forms import CoverForm

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
    cover_form = CoverForm()
    return render(request, 'comics/detail.html', { 'comic': comic, 'cover_form': cover_form })

def add_cover(request, comic_id):
    # create a ModelForm instance using the date in the request.POST
    form = CoverForm(request.POST)
    # validate the form
    if form.is_valid():
        #don't save the form to the db until it has the comic_id assigned
        new_cover = form.save(commit=False)
        new_cover.comic_id = comic_id
        new_cover.save()
    return redirect('detail', comic_id=comic_id)