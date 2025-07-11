from django.urls import path

from .views import (
    RegisterView, LoginView, MeView,
    LogoutView, ChangePasswordView, UpdateProfileView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('me/', MeView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('update-profile/', UpdateProfileView.as_view()),
]

