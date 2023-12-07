from django.urls import path
from .views import education, experience, create_profile, dashboard, login, profile, profiles, register

urlpatterns = [
    path('education/', education, name='education'),
    path('experience/', experience, name='experience'),
    path('create_profile/', create_profile, name='create_profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('profiles/', profiles, name='profiles'),
    path('register/', register, name='register'),
]
