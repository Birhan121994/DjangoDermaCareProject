from django.urls import path
from .views import PatientSignUpView,DermatologistSignUpView,UpdateProfileView,ChangePasswordView
from .views import UserProfileView,UpdateUserProfileView,CreateUserProfileView, UpdateProfileViewforuser
from . import views
from .views import ResetPasswordView, ResetDoneView , ResetPasswordConfirmView, ResetPasswordCompleteView,login_page
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('PatientRegister/',PatientSignUpView.as_view(),name="PatientRegister"),
    path('DermaRegister/',DermatologistSignUpView.as_view(),name="DermaRegister"),
    path('UpdateProfile/',UpdateProfileView.as_view(),name="UpdateProfilePage"),
    path('UpdatePatientProfile/', UpdateProfileViewforuser.as_view(), name="UpdatePatientProfileSetting"),
    path('password/',ChangePasswordView.as_view(), name = "ChangePasswordPage"),
    path('UserProfileInfo/<int:pk>', UserProfileView.as_view(), name = "UserProfileInfoPage"),
    path('UpdateUserProfileInfo/<int:pk>', UpdateUserProfileView.as_view(), name= "UpdateUserProfilePage"),
    path('RoleChoicePage/', views.RoleChoice, name = "RoleChoicePage"),
    path('CreateUserProfile/<int:pk>', CreateUserProfileView.as_view(), name="CreateUserProfilePage"),

    path('password-reset/', ResetPasswordView.as_view(),name='password_reset'),
    path('password-reset/done/', ResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view() ,name='password_reset_confirm'),
    path('password-reset-complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
    path('DermaCare-Login/', views.login_page, name = "login"),
]