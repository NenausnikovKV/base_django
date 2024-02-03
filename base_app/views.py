from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.shortcuts import render


def root(request):
    addresses = {
        "function_view": request.build_absolute_uri(reverse("base_app:function_view")),
        "class_view": request.build_absolute_uri(reverse("base_app:class_view")),
    }
    return render(request, template_name="base_app/root.html", context={"addresses": addresses})


def hello_world(request):
    user = authenticate(username="admin", password="admin")
    if user:
        return HttpResponse(f"hello {user.username}")
    else:
        return HttpResponse("hello world")


class HelloWorld(View):

    @staticmethod
    def get(request):
        return HttpResponse("Hello world")
