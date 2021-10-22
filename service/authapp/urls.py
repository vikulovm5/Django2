from django.urls import path
from .views import authentication, authorization

urlpatterns = [
    path('authentication/', authentication),
    path('authorization/', authorization),
]
