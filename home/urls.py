from django.urls import path
from . import views

app_name = "home"
urlpatterns = [path("home/", views.HomeView.as_view(),name='home')]
urlpatterns = [path("hometemplate/", views.HomeTemplateView.as_view(),name='hometemplate')]
