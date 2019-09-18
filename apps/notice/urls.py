from django.urls import path
from . import views

app_name = "notice"

urlpatterns = [
    path('my_notifications/', views.my_notifications, name="my_notifications"),
    path('my_notification/<int:my_notifications_pk>', views.my_notification, name="my_notification"),
    path('delete_my_read_notifications', views.delete_my_read_notifications, name="delete_my_read_notifications"),
]
