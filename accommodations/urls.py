from django.urls import path
from . import views

app_name = "accommodations"
urlpatterns = [
    path("", views.show_view, name="home"),
    path("<slug:slug>", views.show_view, name="detail"),
    path(
        "accommodations/<int:pk>/create",
        views.CreateItemView.as_view(),
        name="createItem",
    ),
    path(
        "accommodations/<int:pk>/edit", views.EditItemView.as_view(), name="editItem",
    ),
]
