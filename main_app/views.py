from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Comic, Hero
from .forms import CoverForm

class ComicCreate(CreateView):
    model = Comic
    fields = ['name', 'issue', 'writer', 'artist', 'description']

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
    heroes_not_on_the_team = Hero.objects.exclude(id__in = comic.heroes.all().values_list('id'))
    cover_form = CoverForm()
    return render(request, 'comics/detail.html', { 'comic': comic, 'cover_form': cover_form,
    'heroes':heroes_not_on_the_team })

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

def assoc_hero(request, comic_id, hero_id):
    Comic.objects.get(id=comic_id).heroes.add(hero_id)
    return redirect('detail', comic_id=comic_id)

class HeroList(ListView):
  model = Hero

class HeroDetail(DetailView):
  model = Hero

class HeroCreate(CreateView):
  model = Hero
  fields = '__all__'

class HeroUpdate(UpdateView):
  model = Hero
  fields = ['secret_identity', 'power']

class HeroDelete(DeleteView):
  model = Hero
  success_url = '/heroes/'