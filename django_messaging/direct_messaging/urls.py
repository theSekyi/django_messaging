from django.views.generic import TemplateView

from django.urls import path
from .views import inbox


urlpatterns = [
    path("inbox/", inbox, name="inbox"),
]
