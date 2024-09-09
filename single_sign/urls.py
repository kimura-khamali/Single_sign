from django.urls import path
# from .views import SignUpView
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('login/', views.auth_login_view, name='login'),
    # path("login/", views.auth_login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("callback/", views.callback, name='callback'),
    path("register/", views.register, name='register'),
    # path()
    # path('signup/', SignUpView.as_view(), name='signup'),

     
]   