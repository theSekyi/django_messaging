from django.views.generic import TemplateView

from django.urls import path
from direct_messaging.views import inbox


urlpatterns = [
    path("", inbox, name="inbox"),
]
