from django.urls import path

from . import views
app_name = "base_app"

urlpatterns = [
    path("", views.root, name="root"),
    path("function/", views.hello_world, name="function_view"),
    path("class/", views.HelloWorld.as_view(), name="class_view"),

]
