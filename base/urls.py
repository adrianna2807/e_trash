from django.urls import path
from . import views
app_name = 'base'

urlpatterns = [
    path("clients-create-view/", views.ClientCreateView.as_view(), name="clients-create-view"),
    ]