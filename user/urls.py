from django.urls import path, include
from .views import *
urlpatterns = [
    path('user', UserApiView.as_view()),
    path('user/<int:pk>/', UserApiView.as_view()),
    path('t', TransactionApiView.as_view()),
    path('profile/', UserProfileView.as_view()),
]
