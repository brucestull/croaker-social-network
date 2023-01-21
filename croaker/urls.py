from django.urls import path
from django.views.generic.base import RedirectView

from croaker import views


app_name = 'croaker'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='croaker:dashboard')),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('profiles/', views.profile_list, name='profile-list'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile-detail'),
]
