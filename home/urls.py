from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("hometemplate/", views.HomeTemplateView.as_view(), name="hometemplate"),
    path("two/<str:name>/<int:id>/", views.Two.as_view(), name="two"),
    path("cars/", views.CarListView.as_view(), name="cars"),
    path("<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    # path("<slug:my_slug>/", views.CarDetailView.as_view(), name="car_detail"),
    # path(
    #     "<str:name>/<str:owner>/<int:year>/",
    #     views.CarDetailView.as_view(),
    #     name="car_detail",
    # ),
    path("create/", views.CarCreateView.as_view(), name="create"),
    path("carcreate/", views.CarCreateCreateView.as_view(), name="car_create"),
    path("delte/<int:pk>/", views.CarDeleteView.as_view(), name="car_delete"),
]
