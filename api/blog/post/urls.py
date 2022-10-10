from django.urls import path

from blog.post import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:id>', views.SinglePostView.as_view()),
]
