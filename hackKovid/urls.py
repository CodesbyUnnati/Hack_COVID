from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('store/', views.store, name='store'),
    path('guidelines/', views.guide, name='guide'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('product/<stri>', views.products, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
