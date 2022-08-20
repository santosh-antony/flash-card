# cards/urls.py

from django.urls import URLPattern, path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='cards/base.html'),
        name='home'
    ),
]