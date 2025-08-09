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
    path("delete/<int:pk>/", views.CarDeleteView.as_view(), name="car_delete"),
    path("update/<int:pk>/", views.CarUpdateView.as_view(), name="car_update"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path("<int:year>/<int:month>/", views.CarMonth.as_view()),
    # API
    path("carlistapi/", views.CarListAPI.as_view()),
    path("carlistapi/<str:name>/", views.CarSingleAPI.as_view()),
    path("cardeleteapi/<str:str_name>/", views.CarDeleteAPI.as_view()),
    path("createapi/", views.CarCreateAPI.as_view()),
    path("updateapi/<int:pk>/", views.CarUpdateAPI.as_view()),
    path("genericapi/<int:pk>/", views.CarGenericAPI.as_view()),
]
