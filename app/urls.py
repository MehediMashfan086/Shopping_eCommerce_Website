from django.urls import path
from django.utils.translation import templatize
from app import views
from app.forms import LoginForm
from app.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.ProductView.as_view(), name = 'home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', 
    authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customer_registration'),
    path('checkout/', views.checkout, name='checkout'),
    path('twear/', views.TopWear, name='twear'),
    path('twear/<slug:data>', views.TopWear, name='tweardata'),
    path('bwear/', views.BottomWear, name='bwear'),
    path('bwear/<slug:data>', views.BottomWear, name='bweardata'),
    path('camera/', views.Camera, name='camera'),
    path('watch/', views.Watch, name='watch'),
    path('cosmetics/', views.Cosmetics, name='cosmetics'),
    path('bag/', views.Bag, name='bag'),
    path('password_reset/', views.PasswordReset, name='password_reset'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)