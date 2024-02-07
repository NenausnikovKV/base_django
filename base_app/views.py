from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


@login_required()
# @permission_required("base_app.add_name", raise_exception=True)
@permission_required("base_app.can_eat_pizzas", raise_exception=True)
def hello_world(request):
    # user = authenticate(username="admin", password="admin")
    if request.user.is_authenticated:
        user = request.user
        return HttpResponse(f"hello {user.username}")
    else:
        return HttpResponse("hello world")


class HelloWorld(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = []

    @staticmethod
    def get(request):
        return HttpResponse("Hello world")
