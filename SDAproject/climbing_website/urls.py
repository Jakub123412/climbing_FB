from django.urls import path

from . import views, views_admin

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path("", views.HomeView.as_view(), name="home"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("search", views.SearchView.as_view(), name="search"),
    path("review/<int:route_id>", views.RouteReviewView.as_view(), name="review"),

    path("localizations", views_admin.LocalizationListView.as_view(), name="localizations"),
    path("create_localization", views_admin.CreateLocalizationView.as_view(), name="create_localization"),
    path("update_localization/<int:pk>", views_admin.UpdateLocalizationView.as_view(), name="update_localization"),
    path("delete_localization/<int:pk>", views_admin.LocalizationDeleteView.as_view(), name="delete_localization"),

    path("rocks", views.RockListView.as_view(), name="rocks"),
    path("create_rock", views_admin.CreateRockView.as_view(), name="create_rock"),
    path("update_rock/<int:pk>", views_admin.UpdateRockView.as_view(), name="update_rock"),
    path("delete_rock/<int:pk>", views_admin.RockDeleteView.as_view(), name="delete_rock"),
    path("image_rock/<int:rock_id>", views_admin.rock_image, name="image_rock"),

    path("routes", views_admin.RouteListView.as_view(), name="routes"),
    path("create_route", views_admin.CreateRouteView.as_view(), name="create_route"),
    path("update_route/<int:pk>", views_admin.UpdateRouteView.as_view(), name="update_route"),
    path("delete_route/<int:pk>", views_admin.RouteDeleteView.as_view(), name="delete_route"),

    path("reviews", views_admin.ReviewListView.as_view(), name="reviews"),
    path("delete_review/<int:pk>", views_admin.ReviewDeleteView.as_view(), name="delete_review"),
]

