from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('create/', views.render_register_user_form, name='create'),
    path('register/', views.process_register_user_form, name='register'),
    path('login/', views.render_login_user_form, name='login'),
    path('authorize/', views.process_login_user_form, name='authorize'),
]
