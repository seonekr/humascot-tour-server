# urls.py
from django.urls import path
from tourApi import views


urlpatterns = [
    # Tour management
    path("tour/list/", views.TourListAPIView.as_view(), name="tour-list"),
    path("tour/create/", views.TourCreateAPIView.as_view(), name="tour-create"),
    path(
        "tour/detail/<int:pk>/", views.TourRetrieveAPIView.as_view(), name="tour-detail"
    ),
    path(
        "tour/update/<int:pk>/", views.TourUpdateAPIView.as_view(), name="tour-update"
    ),
    path(
        "tour/delete/<int:pk>/", views.TourDestroyAPIView.as_view(), name="tour-delete"
    ),
    # Hotel management
    path("hotel/list/", views.HotelListAPIView.as_view(), name="hotel-list"),
    path("hotel/create/", views.HotelCreateAPIView.as_view(), name="hotel-create"),
    path(
        "hotel/detail/<int:pk>/",
        views.HotelRetrieveAPIView.as_view(),
        name="hotel-detail",
    ),
    path(
        "hotel/update/<int:pk>/",
        views.HotelUpdateAPIView.as_view(),
        name="hotel-update",
    ),
    path(
        "hotel/delete/<int:pk>/",
        views.HotelDestroyAPIView.as_view(),
        name="hotel-delete",
    ),
    # Restaurant management
    path(
        "restaurant/list/",
        views.RestaurantListAPIView.as_view(),
        name="restaurant-list",
    ),
    path(
        "restaurant/create/",
        views.RestaurantCreateAPIView.as_view(),
        name="restaurant-create",
    ),
    path(
        "restaurant/detail/<int:pk>/",
        views.RestaurantRetrieveAPIView.as_view(),
        name="restaurant-detail",
    ),
    path(
        "restaurant/update/<int:pk>/",
        views.RestaurantUpdateAPIView.as_view(),
        name="restaurant-update",
    ),
    path(
        "restaurant/delete/<int:pk>/",
        views.RestaurantDestroyAPIView.as_view(),
        name="restaurant-delete",
    ),
    # Packet management
    path(
        "packet/list/",
        views.PacketListAPIView.as_view(),
        name="packet-list",
    ),
    path(
        "packet/create/",
        views.PacketCreateAPIView.as_view(),
        name="packet-create",
    ),
    path(
        "packet/detail/<int:pk>/",
        views.PacketRetrieveAPIView.as_view(),
        name="packet-detail",
    ),
    path(
        "packet/update/<int:pk>/",
        views.PacketUpdateAPIView.as_view(),
        name="packet-update",
    ),
    path(
        "packet/delete/<int:pk>/",
        views.PacketDestroyAPIView.as_view(),
        name="packet-delete",
    ),
    # Guide management
    path(
        "guide/list/",
        views.GuideListAPIView.as_view(),
        name="guide-list",
    ),
    path(
        "guide/create/",
        views.GuideCreateAPIView.as_view(),
        name="guide-create",
    ),
    path(
        "guide/detail/<int:pk>/",
        views.GuideRetrieveAPIView.as_view(),
        name="guide-detail",
    ),
    path(
        "guide/update/<int:pk>/",
        views.GuideUpdateAPIView.as_view(),
        name="guide-update",
    ),
    path(
        "guide/delete/<int:pk>/",
        views.GuideDestroyAPIView.as_view(),
        name="guide-delete",
    ),
    # Ticket management
    path("ticket/list/", views.TicketListAPIView.as_view(), name="ticket-list"),
    path("ticket/create/", views.TicketCreateAPIView.as_view(), name="ticket-create"),
    path(
        "ticket/detail/<int:pk>/",
        views.TicketRetrieveAPIView.as_view(),
        name="ticket-detail",
    ),
    path(
        "ticket/update/<int:pk>/",
        views.TicketUpdateAPIView.as_view(),
        name="ticket-update",
    ),
    path(
        "ticket/delete/<int:pk>/",
        views.TicketDestroyAPIView.as_view(),
        name="ticket-delete",
    ),
]
