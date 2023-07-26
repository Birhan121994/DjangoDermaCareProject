import os
import pyttsx3
import readtime 
import tempfile
from datetime import date
from django.db import models
from django.urls import reverse
from django.http import request
from django.utils import timezone
from googletrans import Translator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class ChatMessage(models.Model):
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
        
def validate_future_datetime(value):
    if value < timezone.now():
        raise ValidationError('Datetime cannot be in the past.')
def check_valid_derma(value):
    if User.objects.filter(username = value).exists() == False:
        raise ValidationError('Invalid Dermatologist')

class Appointment(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?251?\d{9,15}$', # regular expression pattern for a valid phone number
        message="Invalid Phone number"
    )

    email_regex = RegexValidator(
        regex = r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$",
        message = "Invalid Email Address"
    )
    first_name_regex  = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message = "Invalid first name"
    )
    last_name_regex = RegexValidator(
        regex = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
        message="Invalid last name"
    )
    first_name = models.CharField(max_length=50, validators=[first_name_regex])
    last_name = models.CharField(max_length=50, validators=[last_name_regex])
    phone_no =  models.CharField(
        max_length=15,
        validators=[phone_regex],
        verbose_name='Phone Number'
    )
    email = models.EmailField(max_length=50, validators=[email_regex])
    prefered_date_time = models.DateTimeField(validators=[validate_future_datetime], null=True)
    derma_user = models.CharField(validators = [check_valid_derma], max_length = 50,default='')
    request = models.TextField(blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField("Approve",default=False)
    rejected = models.BooleanField("Reject",default=False)

    def __str__(self):
        return self.first_name
    def validate():
        return message
    class Meta:
        ordering = (['-sent_date'])

class Photo(models.Model):
    name = models.CharField(max_length=100)
    photo_file = models.ImageField(upload_to="All/")

class AtopicDermatitis(models.Model):
    name = models.CharField(max_length=100)
    photo_file = models.ImageField(upload_to="AtopicDermatitis/")

class BasalCellCarcinoma(models.Model):
    name = models.CharField(max_length=100)
    photo_file = models.ImageField(upload_to="BasalCellCarcinoma/")


class User(AbstractUser):
    is_dermatologist = models.BooleanField(default = False)
    is_patient = models.BooleanField(default = False)
    speciality = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100 ,default="")
    phone = models.CharField(max_length = 50,default="")
    agree = models.BooleanField(default = False)
    GENDER = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True, default = "")
    DermaCV_File = models.FileField(upload_to='Documents/', default="")

class Dermatologist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    speciality = models.CharField(max_length = 100,default="")
    agree = models.BooleanField(default = False)
    location = models.CharField(max_length = 100, default="")
    phone = models.CharField(max_length = 50,default="")
    GENDER = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True,  default = "")
    DermaCV_File = models.FileField(upload_to='Documents/', default= "")

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    location = models.CharField(max_length = 100,default="")
    phone = models.CharField(max_length = 50,default="")
    agree = models.BooleanField(default = False)
    GENDER = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True,  default = "")

    def __str__(self):
        return self.user.username

        
class LatestNews(models.Model):
    newsauthor = models.OneToOneField(User, on_delete = models.CASCADE)
    LatestNewsImage = models.ImageField(default='default.jpg',upload_to='latestnews_images')
    newstitle = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=timezone.now)
    sample_content = models.TextField(default="Sample_Content")
    content = models.TextField()

    def __str__(self):
        return self.newstitle 


class OurDermatologists(models.Model):
    admin = models.ManyToManyField(User)
    DermaImages = models.ImageField(upload_to='Dermatologists_images')
    DermaNames = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.DermaNames

class Logo(models.Model):
    admin = models.ManyToManyField(User)
    logo_image = models.ImageField(upload_to = 'WebLogoImageFolder')

class ContentCategory(models.Model):
    category_title = models.CharField(max_length = 100)
    def __str__(self):
        return self.category_title

    def get_absolute_url(self):
        return reverse('DermaBlogPage')


class DermaCategory(models.Model):
    derma_user_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.derma_user_name

    def get_absolute_url(self):
        return reverse('Contact')

class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = RichTextField(blank = True, null=True)
    sub_content = RichTextField(blank = True, null = True)
    content_category = models.CharField(max_length = 100,default = "DermaBlog")
    blog_image = models.ImageField(null = True, blank = True, upload_to = 'DermaBlogImageFolder')
    Bloglikes = models.ManyToManyField(User,related_name = 'Derma_Blogs')
    def get_readtime(self):
      result = readtime.of_text(self.content)
      return result.text 

    def change_voice(engine, language):
        for voice in engine.getProperty('voices'):
            if language in voice.languages:
                engine.setProperty('voice', voice.id)
                return True
    
    def speak_content(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            engine.setProperty('voice', voice.id)
            if "zh" in voice.id:
                print(voice.id)
                
        change_voice(engine, "am_ET")
        engine.say(self.content)
        engine.runAndWait()
        engine.stop()
        return engine
        
    def speak_subcontent(self):
        engine = pyttsx3.init()
        engine.say(self.sub_content)
        engine.runAndWait()
        engine.stop()
        return engine
    def BlogPostTotalLikes(self):
        return self.Bloglikes.count()
    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse('DermaBlogPage')

class BlogComment(models.Model):
    blogpost = models.ForeignKey(BlogPost, related_name = "blogcomments", on_delete = models.CASCADE)
    Commenter_name = models.ForeignKey(User, on_delete = models.CASCADE)
    date_commented = models.DateTimeField(default = timezone.now)
    comment_content = RichTextField(blank = True, null=True)
    # comment_content = models.TextField()

    def __str__(self):
        return str(self.Commenter_name)

class Reply(models.Model):
    comment = models.ForeignKey(BlogComment, related_name='replies',  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default = timezone.now)
    reply = RichTextField(blank = True, null = True)
    # reply = models.TextField()

    def __str__(self):
        return str(self.user)

class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True ,on_delete = models.CASCADE)
    profile_picture = models.ImageField(null = True, blank = True ,upload_to = "UserProfilePictureFolder")
    user_biography = models.TextField()
    first_name = models.CharField(max_length=100 , default = "")
    last_name = models.CharField(max_length = 100, default = "")
    location = models.CharField(max_length = 100, default = "")
    quotes = models.CharField(max_length = 100, default = "" )
    user_facebook = models.CharField(max_length = 100)
    user_google = models.CharField(max_length = 100)
    user_instagram = models.CharField(max_length = 100)
    user_twitter = models.CharField(max_length = 100) 

    def __str__(self):
        return str(self.user)







