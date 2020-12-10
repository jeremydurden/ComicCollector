from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Comic:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, writer, artist, issue, description):
    self.name = name
    self.writer = writer
    self.artist = artist
    self.issue = issue
    self.description = description

comics = [
  Comic('SuperDudes', 'Joe Writer', 'Sally Artist', 14, 'it is a good issue'),
  Comic('SuperLadies', 'Ellen Writer', 'William Artist', 90, 'it is a great issue'),
  Comic('SuperTeam', 'Bonny Writer', 'Rebecca Artist', 72, 'it is a super issue'),
]





def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
  return render(request, 'comics/index.html', { 'comics': comics })