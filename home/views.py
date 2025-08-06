from django.shortcuts import render
from django.views import View
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Car
from .froms import CarCreateForm, CarFormSet
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views as auth_views


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
    model = Car  # object_list
    # queryset = Car.objects.filter(year__lte=2022)
    context_object_name = "cars"
    # ordering ='-year'
    # allow_empty = False # if False show 404 , defult= True

    # def get_queryset(self):
    #     return Car.objects.filter(year__gte=2022)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "sss"
        return context


class CarDetailView(DetailView):
    template_name = "home/detail.html"
    context_object_name = "car"  # object
    model = Car
    # pk_url_kwarg = "my_id"
    # slug_url_kwarg = "my_slug"
    # slug_field = "name"
    # # queryset = Car.objects.filter(year__lte=2022) # 404

    # # def get_queryset(self): # complex query, 404
    # #     return Car.objects.filter(year__gte=2022)

    # def get_object(self, queryset=None):
    #     return Car.objects.get(
    #         name=self.kwargs["name"],
    #         owner=self.kwargs["owner"],
    #         year=self.kwargs["year"],
    #     )


class CarCreateView(FormView):
    template_name = "home/create.html"
    form_class = CarFormSet
    success_url = reverse_lazy("home:cars")

    def form_valid(self, form):
        self._cre_create(form.cleaned_data)
        messages.success(self.request, "create car successfully", "success")
        return super().form_valid(form)

    def _cre_create(self, data):
        Car.objects.create(name=data["name"], year=data["year"], owner=data["owner"])


class CarCreateCreateView(CreateView):
    model = Car
    fields = ["name", "year"]
    template_name = "home/create.html"
    success_url = reverse_lazy("home:cars")

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "nothing"
        )
        car.save()
        messages.success(self.request, "Car created successfully.")
        return super().form_valid(form)


class CarDeleteView(DeleteView):  # id
    model = Car
    success_url = reverse_lazy("home:cars")
    template_name = "home/delete.html"


class CarUpdateView(UpdateView):
    model = Car
    fields = ["name", "year"]
    success_url = reverse_lazy("home:cars")
    template_name = "home/update.html"


class UserLogin(auth_views.LoginView):
    template_name = "home/login.html"

    def get_success_url(self):
        return reverse_lazy("home:cars")
