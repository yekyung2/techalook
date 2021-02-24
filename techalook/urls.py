from django.urls import path
import static
from . import views

app_name = "techalook"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:card_id>/", views.detail, name="detail"),
]
