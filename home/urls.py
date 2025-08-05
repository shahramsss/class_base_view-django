from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("hometemplate/", views.HomeTemplateView.as_view(), name="hometemplate"),
    path("two/<str:name>/<int:id>/", views.Two.as_view(), name="two"),
    path("cars/", views.CarListView.as_view(), name="cars"),
]
