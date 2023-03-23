from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count, Avg
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView, ListView
from .forms import RegisterForm, LoginForm, SearchForm, RouteReviewForm
from .models import Rock, Formation, Route, RouteReview, RouteGrade


# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "climbing_website/register.html"
    success_url = reverse_lazy("login")


class LoginView(FormView):
    template_name = "climbing_website/login.html"
    success_url = reverse_lazy("home")
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error("password", "Niepoprawne dane logowania")
            return super().form_invalid(form)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "climbing_website/home.html"


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        print("Wylogowanie:", request.user.username)
        logout(request)
        return redirect("login")


class SearchView(ListView):
    model = Rock
    form_class = SearchForm
    template_name = "climbing_website/search.html"
    context_object_name = "rocks"

    def get_queryset(self):
        rocks = Rock.objects
        # route = Route.objects
        data = self.request.GET

        region = data.get("region", None)
        if region:
            rocks = rocks.filter(localization__region__contains=region)

        route_name = data.get("route_name", None)
        if route_name:
            rocks = rocks.filter(routes__rout_name=route_name)

        formation = data.get("formation", None)
        if formation:
            rocks = rocks.filter(formation__id=formation)

        insolation = data.get("insolation", None)
        if insolation:
            rocks = rocks.filter(insolation__id=insolation)

        height_min = data.get("height_min", None)
        if height_min:
            rocks = rocks.filter(height__gte=height_min)

        height_max = data.get("height_max", None)
        if height_max:
            rocks = rocks.filter(height__lte=height_max)

        trad = data.get("trad", None)
        if trad == "on":
            rocks = rocks.filter(routes__trad=True)

        return rocks.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class(self.request.GET)
        context["formations"] = Formation.objects.all()
        return context


class RockListView(LoginRequiredMixin, ListView):
    model = Rock
    context_object_name = "rocks"
    template_name = "climbing_website/rocks.html"


class RouteReviewView(LoginRequiredMixin, CreateView):
    form_class = RouteReviewForm
    template_name = "climbing_website/route_review.html"

    def form_valid(self, form):
        route_id = self.kwargs.get("route_id")
        form.instance.route = Route.objects.get(id=route_id)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        route_id = self.kwargs.get("route_id")
        context = super().get_context_data(**kwargs)
        context["object"] = Route.objects.get(id=route_id)
        reviews = RouteReview.objects.filter(route__id=route_id).order_by("-date_create")
        context["reviews"] = reviews
        avg_rate = reviews.aggregate(avg=Avg("user_grade__number"))
        if avg_rate["avg"]:
            context["rate"] = RouteGrade.objects.filter(number=int(avg_rate["avg"])).first().name
        return context

    def get_success_url(self):
        return reverse("review", args=[self.kwargs.get("route_id")])

