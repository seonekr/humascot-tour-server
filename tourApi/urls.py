# urls.py
from django.urls import path
from tourApi import views


urlpatterns = [
    # Tour management
    path('tour/list/', views.TourListAPIView.as_view(), name='tour-list'),
    path('tour/create/', views.TourCreateAPIView.as_view(), name='tour-create'),
    path('tour/detail/<int:pk>/', views.TourRetrieveAPIView.as_view(), name='tour-detail'),
    path('tour/update/<int:pk>/', views.TourUpdateAPIView.as_view(), name='tour-update'),
    path('tour/delete/<int:pk>/', views.TourDestroyAPIView.as_view(), name='tour-delete'),
]
