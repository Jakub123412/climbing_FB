from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL, CASCADE


# Create your models here.
class Country(models.Model):
    country_number = models.CharField(max_length=40)
    country_name = models.CharField(max_length=250)

    def __str__(self):
        return self.country_name


class Formation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Insolation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Localization(models.Model):
    district = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100)
    rock_groups = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=CASCADE, related_name="localizations")

    def __str__(self):
        return f"{self.district} {self.region} {self.subregion} {self.rock_groups}\n"


class Rock(models.Model):
    rock_name = models.CharField(max_length=100)
    photo_map = models.ImageField(upload_to="images/")
    height = models.IntegerField()
    insolation = models.ForeignKey(Insolation, on_delete=CASCADE, related_name="rocks")
    formation = models.ForeignKey(Formation, on_delete=CASCADE, related_name="rocks")
    localization = models.ForeignKey(Localization, on_delete=CASCADE, related_name="rocks")

    def __str__(self):
        return f"{self.rock_name} {self.photo_map} {self.height} {self.insolation} {self.formation}\n"


class Route(models.Model):
    route_number = models.IntegerField()
    rout_name = models.CharField(max_length=100)
    grades = models.CharField(max_length=5)
    autor = models.CharField(max_length=100, null=True, blank=True)
    number_of_glued = models.IntegerField(null=True, blank=True)
    trad = models.BooleanField()
    description = models.CharField(max_length=250, null=True, blank=True)
    rock = models.ForeignKey(Rock, on_delete=CASCADE, related_name="routes")

    def __str__(self):
        return f"{self.rout_name} {self.grades} {self.autor} {self.number_of_glued} {self.trad} {self.description}\n"


class RouteGrade(models.Model):
    name = models.CharField(max_length=5)
    number = models.IntegerField(default=0, )

    def __str__(self):
        return f"{self.id}. {self.name}"


class RouteReview(models.Model):
    user_grade = models.ForeignKey(RouteGrade, on_delete=CASCADE, related_name="reviews")
    user_description = models.CharField(max_length=250)
    route = models.ForeignKey(Route, on_delete=CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=SET_NULL, related_name="reviews", null=True)
    done = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return f" {self.user_grade} {self.user_description} \n"

