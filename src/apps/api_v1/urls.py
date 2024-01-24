from django.urls import path, include


urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path("", include("src.apps.comments.urls")),
]
