from django.urls import path
from . import views
app_name = 'base'

urlpatterns = [
    path("clients-list-view/", views.ClientListView.as_view(), name="clients-list-view"),
    path("clients-detail-view/<pk>", views.ClientDetailView.as_view(), name="clients-detail-view"),
    path("clients-update-view/<pk>", views.ClientUpdateView.as_view(), name="clients-update-view"),
    path("clients-delete-view/<pk>", views.ClientDeleteView.as_view(), name="clients-delete-view"),
    path("clients-model-form-view/", views.ClientModelFormView.as_view(), name = "clients-model-form-view"),
    ]