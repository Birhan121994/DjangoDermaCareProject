from django import forms
from .models import BlogPost
from .models import Appointment
from django.db import transaction
from django.forms import ModelForm
from .models import BlogComment,Reply
from .widget import DateTimePickerInput
from django.forms import ValidationError
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Dermatologist , Patient,ContentCategory, UserProfile


class AppointmentForm(ModelForm):
    
    class Meta:
        model = Appointment
        fields = ('first_name','last_name','phone_no','email','prefered_date_time','derma_user','request')
        labels = {
            'first_name': '',
            'last_name': '',
            'phone_no': '',
            'email': '',
            'prefered_date_time': '',
            'derma_user':'',
            'request': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'AppForm'}),
            'last_name': forms.TextInput(attrs={'class':'AppForm'}),
            'phone_no': forms.TextInput(attrs={'class':'AppForm'}),
            'email': forms.TextInput(attrs={'class':'AppForm'}),
            'prefered_date_time': DateTimePickerInput(attrs={'class':'AppForm','placeholder':'PreferedDateTime'}),
            'derma_user': forms.TextInput(attrs={'class':'AppForm1','placeholder':'DermaUser Name *'}),
            'request': forms.Textarea(attrs={'class':'RequestForm','placeholder':'Request *'}),
        }
       
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(min_length=8, max_length=15, widget=forms.PasswordInput)

def check_valid_patient_username(value):
    if User.objects.filter(username = value).exists() == True:
        raise ValidationError('Patient already exist.')

def check_valid_dermatologist_username(value):
    if User.objects.filter(username = value).exists() == True:
        raise ValidationError('Dermatologist already exist')


class PatientSignUpForm(UserCreationForm):
    username = forms.CharField(max_length = 50, validators = [check_valid_patient_username])
    first_name_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid first name"
    )
    first_name = forms.CharField(max_length = 50, validators=[first_name_regex])
    last_name_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid last name"
    )
    last_name = forms.CharField(max_length = 50, validators=[last_name_regex])
    email_name_regex  = RegexValidator(
        regex = r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$",
        message = "Invalid Email Address"
    )
    email = forms.EmailField(required = True, validators = [email_name_regex])
    locations_name_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid locations"
    )
    location = forms.CharField(max_length = 255, validators=[locations_name_regex])
    phone_regex = RegexValidator(
        regex=r'^\+?251?\d{9,15}$', # regular expression pattern for a valid phone number
        message="Invalid Phone number"
    )
    phone = forms.CharField(max_length = 255, validators=[phone_regex])

    agree = forms.BooleanField()
    GENDER = (('M', 'Male'), ('F', 'Female'))
    gender = forms.ChoiceField(choices=GENDER)
    # gender= forms.ChoiceField(label='What is your Gender?', widget=forms.RadioSelect(choices=GENDER))
    # gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.location = self.cleaned_data.get('location')
        user.phone = self.cleaned_data.get('phone')
        user.agree = self.cleaned_data.get('agree')
        user.gender = self.cleaned_data.get('gender')
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user = user)
        return user

    
choices = ContentCategory.objects.all().values_list('category_title','category_title')
category_choice = []

for items in choices:
    category_choice.append(items)


class DermatologistSignUpForm(UserCreationForm):
    username = forms.CharField(max_length = 50 , validators = [check_valid_dermatologist_username])
    first_name_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid first name"
    )
    first_name = forms.CharField(max_length = 50, validators=[first_name_regex])
    last_name_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid last name"
    )
    last_name = forms.CharField(max_length = 50, validators=[last_name_regex])
    email_name_regex  = RegexValidator(
        regex = r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$",
        message = "Invalid Email Address"
    )
    email = forms.EmailField(required = True, validators = [email_name_regex])
    locations_name_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid locations"
    )
    location = forms.CharField(max_length = 255, validators=[locations_name_regex])
    phone_regex = RegexValidator(
        regex=r'^\+?251?\d{9,15}$', # regular expression pattern for a valid phone number
        message="Invalid Phone number"
    )
    phone = forms.CharField(max_length = 255, validators=[phone_regex])
    # first_name = forms.CharField(max_length = 50)
    # last_name = forms.CharField(max_length = 50)
    # email = forms.EmailField(required = True)
    # location = forms.CharField(max_length = 255)
    # phone = forms.CharField(max_length = 255)
    agree = forms.BooleanField()
    speciality_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid speciality"
    )
    speciality = forms.CharField(max_length = 100, validators = [speciality_regex]) 
    GENDER = (('M', 'Male'), ('F', 'Female'))
    gender = forms.ChoiceField(choices=GENDER)
    DermaCV_File = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.speciality = self.cleaned_data.get('speciality')
        user.gender = self.cleaned_data.get('gender')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.location = self.cleaned_data.get('location')
        user.phone = self.cleaned_data.get('phone')
        user.agree = self.cleaned_data.get('agree')
        user.DermaCV_File = self.cleaned_data.get('DermaCV_File')
        user.is_dermatologist = False
        user.save()
        dermatologist = Dermatologist.objects.create(user = user)
        return user
        
class DermaBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','date_posted','author','content_category','sub_content','content','blog_image')
        widgets = {
            'title':forms.TextInput(attrs={'class':'blog_post_textfiled'}),
            'date_posted':forms.DateTimeInput(attrs={'class':'blog_post_datetimefiled'}),
            'author':forms.TextInput(attrs={'class':'blog_post_authortextfiled','value':"" ,'id':"author" , 'type':'hidden'}),
            'content_category':forms.Select(choices = category_choice ,attrs={'class':'blog_post_authortextfiled'}),
            'content':forms.Textarea(attrs={'class':'blog_post_textarea'}),
            'sub_content':forms.Textarea(attrs={'class':'blog_post_textarea'}),
            # 'blog_image':forms.ImageInput(attrs={'class':'blog_post_textfiled'}),
            # 'author':forms.Select(attrs={'class':'blog_post_authortextfiled'}),
        }

class DermaBlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('Commenter_name','comment_content')
        widgets = {
            'Commenter_name':forms.TextInput(attrs={'value':"" ,'id':"Commenter_name",'type':'hidden'}),
        }
class DermaBlogReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('user','reply')
        widgets = {
            'user':forms.TextInput(attrs={'value':"", 'id':"user",'type':'hidden'}),
        }
class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user','profile_picture','user_biography','first_name','last_name','location','quotes','user_facebook','user_google','user_instagram','user_twitter')
        widgets = {
            'user':forms.TextInput(attrs={'value':"" ,'id':"user" }),
        }
class UpdateDermaBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','date_posted','content_category','sub_content','content','blog_image')
        widgets = {
            'title':forms.TextInput(attrs={'class':'blog_post_textfiled'}),
            'date_posted':forms.DateTimeInput(attrs={'class':'blog_post_datetimefiled'}),
            'content_category':forms.Select(choices = category_choice ,attrs={'class':'blog_post_authortextfiled'}),
            'content':forms.Textarea(attrs={'class':'blog_post_textarea'}),
        }


class UpdateDermatologistProfileForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name','email','location','phone','speciality')
        widgets = {
           'username':forms.TextInput(attrs = {'class':'text_input_filed'}),
           'first_name':forms.TextInput(attrs={'class':'text_input_filed'}),
           'last_name':forms.TextInput(attrs={'class':'text_input_filed'}),
           'email':forms.EmailInput(attrs={'class':'text_input_filed'}),
           'location':forms.TextInput(attrs={'class':'text_input_filed'}),
           'phone':forms.TextInput(attrs={'class':'text_input_filed'}),
           'speciality':forms.TextInput(attrs={'class':'text_input_filed'}),
           
        }
class UpdatePatientProfileSetting(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name','email','location','phone', 'password1', 'password2')
        widgets = {
           'username':forms.TextInput(attrs = {'class':'text_input_filed'}),
           'first_name':forms.TextInput(attrs={'class':'text_input_filed'}),
           'last_name':forms.TextInput(attrs={'class':'text_input_filed'}),
           'email':forms.EmailInput(attrs={'class':'text_input_filed'}),
           'location':forms.TextInput(attrs={'class':'text_input_filed'}),
           'phone':forms.TextInput(attrs={'class':'text_input_filed'}), 
           'password1':forms.PasswordInput(attrs={'class':'text_input_filed'}),
           'password2':forms.PasswordInput(attrs={'class':'text_input_filed'}),
        }