from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('PCs/', views.PCListView.as_view(), name='PCs'),
    path('PCs/<uuid:pk>', views.PCDetailView.as_view(), name='PC-detail'),
]
