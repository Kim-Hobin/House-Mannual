from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms
from accommodations import models as accommodations_models

""" Home View """


def show_home(request):
    if request.user.is_authenticated:
        user = request.user
        accommodations = accommodations_models.Accommodation.objects.filter(host=user)
        return render(request, "users/home.html", {"accommodations": accommodations})
    else:
        return render(request, "users/home.html")


""" Login View"""


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("home:home"))


""" SignUp View """


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        form.save()
        """
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        """
        return super().form_valid(form)


"""
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "admin@gmail.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print("form valid")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print("user exist")
                login(request, user)
                return redirect(reverse("home:home"))
        return render(request, "users/login.html", {"form": form})
"""
