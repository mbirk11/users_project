from django.urls import path
from .views import user_list, user_detail, user_create, user_update, user_delete

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', user_create, name='user_create'),
    path('detail/<int:pk>/', user_detail, name='user_detail'),
    path('update/<int:pk>/', user_update, name='user_update'),
    path('delete/<int:pk>/', user_delete, name='user_delete'),
]