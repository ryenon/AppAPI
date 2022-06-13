from django.conf.urls import url
from django.urls import path
from games import views
from . import views

urlpatterns = [
    path(r'^games/$', views.game_list),
    path(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
]