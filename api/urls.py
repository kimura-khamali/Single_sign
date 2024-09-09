from django.urls import path
from .views import UserListView, LawyerListView,LandSellerListView,LandBuyerListView,UserDetailView,LawyerDetailView,LandBuyerDetailView,LandSellerDetailView
from djoser.views import UserViewSet 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list_view'),
    path('lawyers/', LawyerListView.as_view(), name='lawyer_list_view'),
    path('landsellers/', LandSellerListView.as_view(), name='landseller_list_view'),
    path('landbuyers/', LandBuyerListView.as_view(), name='landbuyer_list_view'),
    path('users/<int:id>/',UserDetailView.as_view(),name='user_detail_view'),
    path('lawyers/<int:id>/', LawyerDetailView.as_view(),name='lawyer_detail_view'),
    path('landsellers/<int:id>/',LandSellerDetailView.as_view(),name='landseller_detail_view'),
    path('landbuyers/<int:id>/', LandBuyerDetailView.as_view(),name='landbuyer_detail_view'),
    path('users/activation/', UserViewSet.as_view({'post': 'activation'}), name='user-activation'),
    path('users/me/', UserViewSet.as_view({'get': 'me'}), name='user-me'),

    # path('users/me/', UserViewSet.as_view({'get': 'me'}), name='user-me'),
    path('users/resend_activation/', UserViewSet.as_view({'post': 'resend_activation'}), name='user-resend-activation'),
    path('users/reset_password/', UserViewSet.as_view({'post': 'reset_password'}), name='user-reset-password'),
    path('users/reset_password_confirm/', UserViewSet.as_view({'post': 'reset_password_confirm'}), name='user-reset-password-confirm'),
    path('users/reset_username/', UserViewSet.as_view({'post': 'reset_username'}), name='user-reset-username'),
    path('users/reset_username_confirm/', UserViewSet.as_view({'post': 'reset_username_confirm'}), name='user-reset-username-confirm'),
    path('users/set_password/', UserViewSet.as_view({'post': 'set_password'}), name='user-set-password'),
    path('users/set_username/', UserViewSet.as_view({'post': 'set_username'}), name='user-set-username'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    
]