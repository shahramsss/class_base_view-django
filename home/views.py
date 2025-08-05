from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DetailView
from .models import Car


class HomeView(View):
    # http_method_names = ['post',]
    def get(self, request):
        return render(request, "home/home.html")

    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers["host"] = "localhost"
        response.headers["user"] = request.user
        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        super().http_method_not_allowed(request, *args, **kwargs)
        return render(request, "method_not_allowd.html")


class HomeTemplateView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = Car.objects.all()
        return context


class Two(RedirectView):
    # url = 'google.com' = add string to url
    # url = "https://google.com"
    pattern_name = "home:home"
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print("*" * 90)
        print("proccesing redirect url")
        print(kwargs["name"])
        print(kwargs["id"])
        kwargs.pop("name")
        kwargs.pop("id")
        return super().get_redirect_url(*args, **kwargs)


class CarListView(ListView):
    template_name = "home/home.html"
    # model = Car # object_list
    # queryset = Car.objects.filter(year__lte=2022)
    context_object_name = "cars"
    # ordering ='-year'
    # allow_empty = False # if False show 404 , defult= True

    def get_queryset(self):
        return Car.objects.filter(year__gte=2022)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "sss"
        return context


class CarDetailView(DetailView):
    template_name = "home/detail.html"
    context_object_name = "car"  # object
    model = Car
    slug_url_kwarg = 'my_slug'
    slug_field = 'name'
