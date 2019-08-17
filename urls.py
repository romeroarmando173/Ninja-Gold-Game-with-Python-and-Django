from django.conf.urls import url           # DON NOT ADD AN s AT THE END OF URL
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^find_gold$',views.find_gold),       #look at how these urls point in different directions
]