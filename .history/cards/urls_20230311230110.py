from django.urls import path
from django.views.generic import TemplateView

from . import v
urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="cards/base.html"),
        name="home"
    ),
]