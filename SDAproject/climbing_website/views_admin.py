from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import LocalizationForm, RockForm, RouteForm
from .models import Localization, Rock, Route, RouteReview

admin_required = method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch') #sprawdza czy użytkownik jest superuserem


@admin_required
class CreateLocalizationView(LoginRequiredMixin, CreateView):
    form_class = LocalizationForm
    template_name = "climbing_website/create_localization.html"
    success_url = reverse_lazy("localizations")


@admin_required
class UpdateLocalizationView(LoginRequiredMixin, UpdateView):
    form_class = LocalizationForm
    model = Localization
    template_name = "climbing_website/create_localization.html"
    success_url = reverse_lazy("localizations")


@admin_required
class LocalizationListView(LoginRequiredMixin, ListView):
    model = Localization
    context_object_name = "localizations"
    template_name = "climbing_website/localizations.html"


@admin_required
class LocalizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Localization
    success_url = reverse_lazy("localizations")
    template_name = "climbing_website/delete_localization.html"


@admin_required
class CreateRockView(LoginRequiredMixin, CreateView):
    form_class = RockForm
    template_name = "climbing_website/create_rock.html"
    success_url = reverse_lazy("rocks")


@admin_required
class UpdateRockView(LoginRequiredMixin, UpdateView):
    form_class = RockForm
    model = Rock
    template_name = "climbing_website/create_rock.html"
    success_url = reverse_lazy("rocks")


@admin_required
class RockDeleteView(LoginRequiredMixin, DeleteView):
    model = Rock
    success_url = reverse_lazy("rocks")
    template_name = "climbing_website/delete_rock.html"


def rock_image(request, rock_id):
    rock = Rock.objects.get(id=rock_id)
    if not rock:
        return HttpResponseNotFound("Rock not found")

    with open(str(rock.photo_map), "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


@admin_required
class CreateRouteView(LoginRequiredMixin, CreateView):
    form_class = RouteForm
    template_name = "climbing_website/create_route.html"
    success_url = reverse_lazy("routes")


@admin_required
class UpdateRouteView(LoginRequiredMixin, UpdateView):
    form_class = RouteForm
    model = Route
    template_name = "climbing_website/create_route.html"
    success_url = reverse_lazy("routes")


@admin_required
class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    context_object_name = "routes"
    template_name = "climbing_website/routes.html"


@admin_required
class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy("routes")
    template_name = "climbing_website/delete_route.html"


@admin_required
class ReviewListView(LoginRequiredMixin, ListView):
    queryset = RouteReview.objects.order_by("-date_create")
    context_object_name = "reviews"
    template_name = "climbing_website/reviews.html"


@admin_required
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = RouteReview
    success_url = reverse_lazy("reviews")
    template_name = "climbing_website/delete_review.html"
