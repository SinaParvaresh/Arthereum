from django.urls import path

from . import views

app_name = "backend"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login', views.Login.as_view(), name="login"),
    path('accounts/register', views.Register, name="register"),
    path('accounts/data/check/<str:address>', views.check_account, name="check"),
    path('profile/<int:id>', views.profile, name="profile"),
]
