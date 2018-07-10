# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
    if "word" not in request.session:
        request.session["word"] = ""
    return render(request,'random_word_generator/index.html')

def random_word(request):
    request.session["word"] = get_random_string(length=14, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    request.session["count"] += 1
    return redirect('/')
    # response = "Random Word Route is Working!"
    # return HttpResponse(response)
def reset(request):
    del request.session['word']
    del request.session['count']
    return redirect('/')
    
    
