from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.db import models
from django.utils import timezone
from .models import Playlist
# Create your views here.

def index(request):
	playlists = Playlist.objects.all()
	years = list()
	for p in playlists:
		if p.Year in years:
			pass
		else:
			years.append(p.Year)
	return render(request,'index.html',{'years':years})


def years(request,year):
	playlists = Playlist.objects.all().filter(Year = year)
	return render(request,'years.html',{'playlists':playlists, 'year':year})