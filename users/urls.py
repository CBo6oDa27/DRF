from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentViewSet, UserCreateApiView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name
router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payments")


urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="users_list"),
    path("detail/<int:pk>", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("edit/<int:pk>", UserUpdateAPIView.as_view(), name="user_edit"),
    path("delete/<int:pk>", UserDestroyAPIView.as_view(), name="user_delete"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
] + router.urls
