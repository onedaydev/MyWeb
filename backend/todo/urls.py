from django.urls import path

from .views import *

urlpatterns = [
    path('todo/',TodosAPIView.as_view()),
    path('todo/<int:pk>/', TodoAPIView.as_view()),
]