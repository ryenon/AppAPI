from django.conf.urls import url
from django.urls import path, re_path
#from games import views
from . import views

urlpatterns = [
    re_path('game_list/', views.game_list),
    re_path('game_detail/(?P<pk>[0-9]+)/', views.game_detail),
]