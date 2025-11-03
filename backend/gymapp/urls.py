from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ping, MemberViewSet, RegisterView

router = DefaultRouter()
router.register(r'members', MemberViewSet, basename='member')

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('', include(router.urls)),
]
