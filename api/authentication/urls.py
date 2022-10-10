from django.urls import include, path

from authentication import views

urlpatterns = [
    path('login', views.SignIn.as_view())
]
