from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserApiView)
router.register(r"transaction", TransactionApiView)

