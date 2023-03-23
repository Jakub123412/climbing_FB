from django.contrib import admin

# Register your models here.
from .models import Country, Route, RouteReview, Rock, RouteGrade, Localization, Formation, Insolation

admin.site.register(Country)
admin.site.register(Route)
admin.site.register(RouteReview)
admin.site.register(Rock)
admin.site.register(RouteGrade)
admin.site.register(Localization)
admin.site.register(Formation)
admin.site.register(Insolation)
