from django.urls import path
from .views import register_view, profiles_view, profile_detail_view
from . import views


urlpatterns = [
    path('register/', register_view, name='register'),
    path('profiles/', profiles_view, name='profiles'),
    path('profiles/<int:id>/', profile_detail_view, name='profile-detail'),
    path('profile/<int:id>/', views.profile_detail_view, name='profile-detail'),
]