# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#/products > index method
def index(request):
    return HttpResponse("Hello World! <br>This is my fisrt dJango app...")


def newproducts(request):
    return HttpResponse("Hello <br><br>This is new product page!");