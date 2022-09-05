from django.urls import path

from . import views

urlpatterns = [
    # ex: /roster/
    path('', views.index, name='index'),
]