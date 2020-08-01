from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name='api-overview'),
    path('list/',views.carlist, name='car-list'),
    path('post/',views.carCreate, name='create'),
    path('update/<str:pk>',views.carUpdate, name='update'),
    path('delete/<str:pk>',views.carDelete, name='delete'),
]