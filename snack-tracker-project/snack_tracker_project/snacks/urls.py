from django.urls import path
from .views import HomeView,SnackListView,SnackDetailView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('snacks-list',SnackListView.as_view(), name='snacks_list'),
    path('detail-view/<int:pk>',SnackDetailView.as_view(), name='snack_detail'),

]