from django.urls import path
from .views import get_users, create_user, user_detail

urlpatterns = [
    path('user/', get_users, name='get_users'),
    path('user/create/', create_user, name='create_user'),
    path('user/<int:pk>', user_detail, name='user_detail')
]