from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:techblog_id>/", views.detail),
]