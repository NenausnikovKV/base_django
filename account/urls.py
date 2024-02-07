from django.urls import path, include

from . import views

app_name = "account"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("local_login/", views.ContactFormView.as_view(), name="local_login"),
    path("thanks/", views.redirect_stump, name="redirect_stump"),
]
