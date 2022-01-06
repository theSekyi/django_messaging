from django.views.generic import TemplateView

from django.urls import path
from direct_messaging.views import inbox, search_users_to_dm


urlpatterns = [
    path("", inbox, name="inbox"),
    path("dm/", search_users_to_dm, name="search_users"),
]
