from django.urls import path
from .views import success

from django.views.generic import TemplateView
from django.conf.urls import url


urlpatterns = [
    path('', TemplateView.as_view(template_name="auth.html")),
    url(r'^test-site/success/', success),
]