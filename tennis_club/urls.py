from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('home/', views.home_view, name='home'),  
    path('accounts/', include('accounts.urls')),
    path('', views.home_redirect, name='home_redirect'),  
    path('reservations/', include('courts.urls')),  
    path('trening/', views.training_view, name='trening'),
    path('cennik/', views.pricing_view, name='cennik'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  
    path('logout/', views.logout_view, name='logout'),  
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
