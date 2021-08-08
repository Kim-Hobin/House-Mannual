from django.shortcuts import render
from . import models
from users import models as user_models
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

""" Client View """


def show_view(request, slug):
    accommodation = models.Accommodation.objects.filter(slug=slug)

    print(type(accommodation.get().get_attractions()))
    return render(
        request,
        "view.html",
        context={
            "accommodations": accommodation,
            "attractions": accommodation.get().get_attractions(),
        },
    )


""" Create accommodation """


class CreateItemView(LoginRequiredMixin, FormView):
    template_name = "accommodations/createItem.html"
    form_class = forms.CreateItemView
    success_url = reverse_lazy("home:home")

    def get_initial(self):
        user = user_models.User.objects.filter(id=self.kwargs["pk"])[0]
        initial = super().get_initial()
        initial["host"] = user
        return initial

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

    def get_object(self, queryset=None):
        user = get_object_or_404(models.User, pk=self.kwargs["pk"])
        return user


""" Edit accommodation """


class EditItemView(LoginRequiredMixin, UpdateView):
    template_name = "accommodations/editItem.html"
    success_url = reverse_lazy("home:home")
    fields = (
        "name",
        "avatar",
        "description",
        "background_image",
        "address",
        "phone_number",
        "check_in",
        "check_out",
        "wifi",
        "facility",
        "recycle",
        "house_rule",
        "content",
        "slug",
    )

    def get_object(self, queryset=None):
        accommodation = get_object_or_404(models.Accommodation, pk=self.kwargs["pk"])
        return accommodation
