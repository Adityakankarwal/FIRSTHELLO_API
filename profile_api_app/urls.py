from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", views.viewsetHello, basename="hello-viewset")
router.register("profile", views.UsreProfileViewSet)

urlpatterns = [
    path('hello-view/', views.ApiviewHello.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
]