from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import MainPageView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', MainPageView.as_view(), name="main-page"),
]
