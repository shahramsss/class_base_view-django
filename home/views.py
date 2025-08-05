from django.shortcuts import render
from django.views import View


class HomeView(View):
    def post(self, request):
        return render(request, "home/home.html")

    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers["host"] = "localhost"
        response.headers["user"] = request.user
        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        return render(request ,'method_not_allowd.html')