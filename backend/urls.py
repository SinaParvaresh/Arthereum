from django.urls import path

from . import views

app_name = "backend"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login', views.Login.as_view(), name="login"),
    path('accounts/register', views.Register, name="register"),
    path('accounts/data/check/<str:address>', views.check_account, name="check"),
    path('profile/<int:id>', views.profile, name="profile"),
    path('auctions/list', views.auction, name="auction"),
    path('transaction/<str:address>', views.Transaction.as_view(), name="transaction"),
    path('NFT/details/<int:pk>', views.detail, name="details"),
    path('NFT/makeoffer/<int:pk>/<int:num>', views.make_offer, name="make_offer"),
    path('NFT/upload', views.Upload.as_view(), name="upload"),
]
