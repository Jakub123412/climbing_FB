from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Localization, Rock, Route, Formation, Insolation, RouteReview


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class LocalizationForm(ModelForm):
    class Meta:
        model = Localization
        fields = "__all__"


class RockForm(ModelForm):
    class Meta:
        model = Rock
        fields = "__all__"


class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = "__all__"


class SearchForm(forms.Form):
    region = forms.CharField(max_length=200, required=False)
    route_name = forms.CharField(max_length=200, required=False)
    formation = forms.ChoiceField(required=False,
                                  choices=((f.id, f.name) for f in
                                           [Formation(id="", name="all")] + list(Formation.objects.all())))
    insolation = forms.ChoiceField(required=False,
                                   choices=((f.id, f.name) for f in
                                            [Formation(id="", name="all")] + list(Insolation.objects.all())))
    height_min = forms.IntegerField(required=False, min_value=0)
    height_max = forms.IntegerField(required=False, min_value=0)
    trad = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.input_type != 'checkbox':
                visible.field.widget.attrs['class'] = 'form-control'
            else:
                visible.field.widget.attrs["data-toggle"] = "toggle"


class RouteReviewForm(forms.ModelForm):
    class Meta:
        model = RouteReview
        fields = ["user_grade", "user_description"]
        widgets = {
            "user_description": forms.Textarea
        }