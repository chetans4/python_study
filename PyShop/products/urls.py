
"""
@auther Chetan
"""

#from django.url import path, include
from django.conf.urls import url
#we are using from . even the views module in current folder (import views) because views is a kind of generic name 
# so it is possible python can take any other library depending upon priority
from . import views


urlpatterns = [
    # /products is the root of products app
    #path("", views.index) #We are not calling views.index we are only refrencing it because django will take care of calling
    url('', views.index, name='Products home'),
    url('new', views.newproducts, name='New Products page')
]