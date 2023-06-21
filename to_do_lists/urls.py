
from django.urls import path,include
from rest_framework import routers
from .views import to_do_viewSet


router = routers.DefaultRouter()
router.register(r'to_do',to_do_viewSet)

urlpatterns = [
    path('',include(router.urls))
]
