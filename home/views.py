from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
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
