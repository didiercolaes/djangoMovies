# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf.settings import PROJECT_ROOT

# Create your views here.
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def index(request):
    #Open the file back and read the contents
    f=open("movies.txt", "r")
    fl =f.readlines()
    for x in fl:
        movies.append(x)
    return render(request,'templates/index.html',{'movies': movies})

#rediscommands
# set movies "the godfather"

@cache_page(CACHE_TTL)
def post(request, name):



