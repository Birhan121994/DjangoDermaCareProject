from django.shortcuts import render,get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from DermaCareApp.forms import PatientSignUpForm,DermatologistSignUpForm, LoginForm
from DermaCareApp.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from DermaCareApp.models import UserProfile
from DermaCareApp.forms import UpdateDermatologistProfileForm, CreateUserProfileForm, UpdatePatientProfileSetting
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'{user.username}'
                return redirect('HomePage')
            else:
                message = 'Please enter the correct username and password for a user account.Note that both fields may be case-sensitive.'

    return render(
        request, 'registration/login.html', context={'form': form, 'message': message})



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "DermaCareApp/home.html" 

def RoleChoice(request):
    return render(request, 'registration/RoleChoice.html',{})

class CreateUserProfileView(generic.CreateView):
    model = UserProfile
    template_name = 'registration/CreateUserProfile.html'
    form_class = CreateUserProfileForm
    success_url = reverse_lazy('DermaBlogPage')

class UpdateUserProfileView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/UpdateUserProfile.html'
    fields = ['profile_picture','user_biography','user_facebook','user_google','user_instagram','user_twitter']
    success_url = reverse_lazy('DermaBlogPage')


class UserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/UserProfileDetailInfo.html'

    def get_context_data(self,*args,**kwargs):
        # category_menu = ContentCategory.objects.all()
        value= super(UserProfileView,self).get_context_data(*args,**kwargs)
        user_value = get_object_or_404(UserProfile,id=self.kwargs['pk'])
        value['user_value'] = user_value
        return value


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/Change_Password.html'
    success_url = reverse_lazy('login')


class ResetPasswordView(PasswordResetView):
    template_name='registration/password_reset_form_one.html'
    success_url= reverse_lazy('password_reset_done')    

class ResetDoneView(PasswordResetDoneView):
    template_name='registration/password_reset_done_one.html'
    success_url = reverse_lazy('password_reset_confirm')

class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name='registration/password_reset_confirm_one.html'
    success_url=reverse_lazy('login')

class ResetPasswordCompleteView(TemplateView):
    template_name='registration/password_reset_complete.html'



class PatientSignUpView(generic.CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/PatientRegister.html'
    success_url = reverse_lazy('login')


class DermatologistSignUpView(generic.CreateView):
    model = User
    form_class = DermatologistSignUpForm
    template_name = 'registration/DermaRegister.html'
    success_url = reverse_lazy('login')


class UpdateProfileView(generic.UpdateView):
    model = User
    form_class = UpdateDermatologistProfileForm
    template_name = 'registration/Update_Profile.html'
    success_url = reverse_lazy('HomePage')

    def get_object(self):
        return self.request.user

class UpdateProfileViewforuser(generic.UpdateView):
    model = User
    form_class = UpdatePatientProfileSetting
    template_name = 'registration/UpdatePatientProfileSetting.html'
    success_url = reverse_lazy('HomePage')

    def get_object(self):
        return self.request.user

