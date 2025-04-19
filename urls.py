from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pests-diseases/', views.pest_disease_list, name='pest_disease_list'),
    re_path(r'^pests-diseases/(?P<issue_name>[\w\s]+)/$', views.pest_disease_detail, name='pest_disease_detail'),
    path('about/', views.about, name='about'),
]