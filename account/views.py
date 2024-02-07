from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import LoginForm


def user_login(request):
    if request.method != 'POST':
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            form = LoginForm()
            return render(request, 'account/login.html', {'form': form})

        cleaned_data = form.cleaned_data
        user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
        if user is None:
            return render(request, 'account/login.html', {'form': form, "error_message": "Invalid login"})
        if not user.is_active:
            return render(request, 'account/login.html', {'form': form, "error_message": "Disabled accoun"})
        login(request, user)
        return HttpResponse("successful login ")


class ContactFormView(FormView):
    template_name = "account/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("account:redirect_stump")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
        if user is None:
            return render(self.request, 'account/login.html', {'form': form, "error_message": "Invalid login"})
        if not user.is_active:
            return render(self.request, 'account/login.html', {'form': form, "error_message": "Disabled account"})
        login(self.request, user)
        return super().form_valid(form)


def redirect_stump(request):
    return HttpResponse("Thanks")


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
