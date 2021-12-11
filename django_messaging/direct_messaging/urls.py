from django.views.generic import TemplateView

from django.urls import path


urlpatterns = [
    path("inbox/", TemplateView.as_view(template_name="direct_messaging/inbox.html"), name="home"),
]
