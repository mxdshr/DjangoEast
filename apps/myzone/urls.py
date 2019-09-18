from django.urls import path
from . import views

app_name = "myzone"

urlpatterns = [
    path('talk/', views.TalkView.as_view(), name='talk'),
]
