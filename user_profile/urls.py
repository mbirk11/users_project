from django.urls import path
from .views import user_list, user_detail, user_create, user_update, user_delete

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:pk>/', user_detail, name='user_detail'),
    path('create/', user_create, name='user_create'),
    path('<int:pk>/update/', user_update, name='user_update'),
    path('<int:pk>/delete/', user_delete, name='user_delete'),
]