from django.urls import path
from . import views

app_name="comment"

urlpatterns = [
    path('update_comment', views.update_comment, name ='update_comment'),
]

