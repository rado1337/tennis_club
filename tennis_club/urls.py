from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views  # Importujemy widoki z głównego folderu

# Definicja ścieżek URL
urlpatterns = [
    path('admin/', admin.site.urls),  # Ścieżka do panelu administracyjnego
    path('home/', views.home_view, name='home'),  # Główna strona pod URL /home
    path('', views.home_redirect, name='home_redirect'),  # Przekierowanie głównego URL na /home/
    path('reservations/', include('courts.urls')),  # Przekierowanie do aplikacji 'courts'
    path('trening/', views.training_view, name='trening'),
    path('cennik/', views.pricing_view, name='cennik'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  # Dodajemy bezpośrednią ścieżkę do rejestracji
    path('logout/', views.logout_view, name='logout'),  # Dodano ścieżkę do wylogowania
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Dodanie obsługi plików multimedialnych w trybie debugowania
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
