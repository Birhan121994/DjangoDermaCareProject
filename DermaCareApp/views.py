from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import LatestNews
from .models import OurDermatologists,BlogPost, BlogComment , Reply
from .forms import DermaBlogPostForm
from .forms import UpdateDermaBlogPostForm
from django.urls import reverse_lazy
from .models import Patient, Dermatologist,User, ContentCategory
from django.contrib.auth import login as auth_login
from django.views.generic import CreateView
from .forms import PatientSignUpForm, DermatologistSignUpForm, DermaBlogCommentForm , DermaBlogReplyForm
from django.urls import reverse_lazy,reverse
import pyttsx3
import streamlit as st
import sqlite3
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from django.template import Context
from django.template.loader import render_to_string, get_template
from .models import Dermatologist,Photo,BasalCellCarcinoma,AtopicDermatitis
from .forms import AppointmentForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import zipfile
from io import BytesIO
from django.shortcuts import render
from django.shortcuts import render
from . import processor
import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView, CreateView , UpdateView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from .models import Dermatologist
from .forms import AppointmentForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.core.mail import send_mail

def chatview(request):
    return render(request, 'DermaCareApp/Chathome.html')

def chatbot_response(request):
    if request.method == 'POST':
        the_question = request.POST.get('question')

        response = processor.chatbot_response(the_question)

        return HttpResponse(json.dumps({"response": response}), content_type='application/json')

def download_photos(request):
    if request.method == "POST":
        photos = Photo.objects.all()
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for photo in photos:
                photo_data = photo.photo_file.read()
                zip_file.writestr(f"{photo.id}.jpg", photo_data)
        response = HttpResponse(zip_buffer.getvalue(), content_type="application/x-zip-compressed")
        response["Content-Disposition"] = "attachment; filename=AllType.zip"
        return response
    else:
        return render(request, "DermaCareApp/Gallery.html")

def download_atopic_photos(request):
    if request.method == "POST":
        photos = AtopicDermatitis.objects.all()
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for photo in photos:
                photo_data = photo.photo_file.read()
                zip_file.writestr(f"{photo.id}.jpg", photo_data)
        response = HttpResponse(zip_buffer.getvalue(), content_type="application/x-zip-compressed")
        response["Content-Disposition"] = "attachment; filename=AtopicDermatitis.zip"
        return response
    else:
        return render(request, "DermaCareApp/Gallery.html")

def download_basalcell_photos(request):
    if request.method == "POST":
        photos = BasalCellCarcinoma.objects.all()
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for photo in photos:
                photo_data = photo.photo_file.read()
                zip_file.writestr(f"{photo.id}.jpg", photo_data)
        response = HttpResponse(zip_buffer.getvalue(), content_type="application/x-zip-compressed")
        response["Content-Disposition"] = "attachment; filename=Basal.zip"
        return response
    else:
        return render(request, "DermaCareApp/Gallery.html")

class GalleryTemplateView(TemplateView):
    template_name = "DermaCareApp/Gallery.html"
class AtopicDermatisView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/AtopicDermatitis.html"
class BasalCellCarcinomaTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/BasalCellCarcinoma.html"
class BenignKeratosisTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/BenignKeratosis.html"
class EczemaTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/Eczema.html"
class MelanocyticNeviTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/MelanocyticNevi.html"
class MelanomaTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/Melanoma.html"
class PsorasisTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/Psorasis.html"
class SeborrheicKeratosisTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/SeborrheicKeratosis.html"
class TineaRingwormTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/TineaRingworm.html"
class WartsMolluscumTemplateView(TemplateView):
    template_name = "DermaCareApp/DiseaseCatagory/WartsMolluscum.html"
class Download(TemplateView):
    template_name = "DermaCareApp/Download.html"

def servicehomeview(request):
    return render(request, 'DermaCareApp/Service_home.html',{})

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        user_value = str(user_input)
        chatbot = ChatBot('DermaCare Customer Service Bot')
        response = chatbot.get_response(user_input)
        bot_value= str(response)
        conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/DataStoreFolder/ChatBot.db')
        cursor = conn.cursor()
        conn.execute("""INSERT INTO chatbotdataholder (user_chat_input,bot_chat_response) VALUES(?,?)""", (user_value, bot_value))
        conn.commit()
        cursor.close()
        conn.close()

        conn2 = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/DataStoreFolder/ChatBot.db')
        cursor2 = conn2.cursor()
        cursor2.execute('''SELECT * FROM chatbotdataholder''') 
        result = cursor2.fetchall()
        conn2.commit()
        cursor2.close()
        conn2.close()
        return render(request, 'DermaCareApp/customer_service_bot.html', {'response': response, 'user_input':user_input,'result':result})


def streamlit_view(request):
    return render(request,'DermaCareApp/streamlit.html')

now = datetime.now()

def request_appointment(request):
    submitted = False
    model = Appointment
    first_name = request.POST.get("first_name")

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, f"Dear {first_name}, thanks for making an appointment, we will email you ASAP!")
            return HttpResponseRedirect('/Contact?submitted=True')
    else:
        form = AppointmentForm
        if 'submitted' in request.GET:
            submitted = True
            form = AppointmentForm
    return render(request,
    'DermaCareApp/contact.html',{
    'form':form,
    'current_day': now.day,

    })

class ManageAppointmentTemplateView(ListView):
    template_name = "DermaCareApp/manage-appointment.html"
    model = Appointment
    context_object_name = "appointments"
    # paginate_by = 6
   
    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        approve = request.POST.get("approve")
        reject = request.POST.get("reject")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted_date = request.POST.get("date")
        appointment.save() 
        
        if approve:
            appointment.accepted = True
            appointment.save()
            message = get_template('DermaCareApp/email.html').render()
            email = EmailMessage(
                "About your appointment",
                message,
                settings.EMAIL_HOST_USER,
                [appointment.email],
            )
            email.content_subtype = "html"
            email.send()
            return HttpResponseRedirect(request.path)
            
        elif reject:
            appointment.rejected = True
            appointment.save()
            message = get_template('DermaCareApp/decline_appo.html').render()
            email = EmailMessage(
                "About your appointment",
                message,
                settings.EMAIL_HOST_USER,
                [appointment.email],
            )
            email.content_subtype = "html"
            email.send()
            return HttpResponseRedirect(request.path)

    def get_context_data(self,*args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        appointme = Appointment.objects.all()
        context.update({
            "title":"Manage Appointmnets"
        })
        return context
    

def adminview(request):
    return render(request, 'templates/admin/base.html',{})
def searchview(request):
    if request.method == 'POST':
        searched_value = request.POST['search']
        blog_search_value = BlogPost.objects.filter(title = searched_value )
        blog_category_value = BlogPost.objects.filter(content_category = searched_value)
        count_value =  BlogPost.objects.filter(title = searched_value ).count
        count_value_two = BlogPost.objects.filter(content_category = searched_value)
        return render(request, 'DermaCareApp/search.html', {'searched_value':searched_value, 'blog_search_value':blog_search_value,'count_value':count_value, 'blog_category_value':blog_category_value,'count_value_two':count_value_two})
    else:
        return render(request, 'DermaCareApp/search.html', {})

def about(request):
    return render(request,'DermaCareApp/about.html')
def services(request):
    return render(request, 'DermaCareApp/take.html')

def home(request):
    display = {
        'LatestNews':LatestNews.objects.all(),
        'OurDermatologists':OurDermatologists.objects.all(),
    }
    return render(request, "DermaCareApp/home.html",display)

def FilterBlogPostCategoriesView(request,FilterCategory):
    catagorie_list = BlogPost.objects.filter(content_category=FilterCategory.replace('-',' '))
    return render(request, 'DermaCareApp/BlogCategories.html',{'FilterCategory':FilterCategory.title().replace('-',' '),'catagorie_list':catagorie_list})


def BlogLikeView(request,pk):
    blog_post = get_object_or_404(BlogPost,id=request.POST.get('post_id'))
    blog_post_liked = False
    if blog_post.Bloglikes.filter(id = request.user.id).exists():
        blog_post.Bloglikes.remove(request.user)
        blog_post_liked = False
    else:
        blog_post.Bloglikes.add(request.user) 
        blog_post_liked = True

    
    return HttpResponseRedirect(reverse('DermaBlogDetailsPage',args=[str(pk)]))

class DermaBlogView(ListView):
    model = BlogPost
    template_name = 'DermaCareApp/DermatologistBlog.html'
    ordering=['-date_posted']


    def get_context_data(self,*args,**kwargs):
        category_menu = ContentCategory.objects.all()
        category_value = super(DermaBlogView,self).get_context_data(*args,**kwargs)
        category_value['category_menu'] = category_menu
        return category_value



class DermaBlogDetailView(DetailView):
    model = BlogPost
    template_name = 'DermaCareApp/DermaBlogDetailPage.html'
    

    def get_context_data(self,*args,**kwargs):
        category_menu = ContentCategory.objects.all()
        category_value = super(DermaBlogDetailView,self).get_context_data(*args,**kwargs)
        like_objects = get_object_or_404(BlogPost,id=self.kwargs['pk'])
        like_value = like_objects.BlogPostTotalLikes()

        category_value['num_visits'] = self.request.session['num_visits']
        blog_liked = False
        no_dislikes = 0
        if like_objects.Bloglikes.filter(id = self.request.user.id).exists():
            blog_liked = True
        else:
            no_dislikes = no_dislikes + 1
        category_value['category_menu'] = category_menu
        category_value['like_value'] = like_value
        category_value['blog_liked'] = blog_liked
        category_value['no_dislikes'] = no_dislikes
        return category_value
    def get(self, request, *args, **kwargs):
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        return super().get(request, *args, **kwargs)

class AudioDermaBlogDetailView(DetailView):
    model = BlogPost
    template_name = 'DermaCareApp/DermaBlogAudioReader.html'

    def get_context_data(self,*args,**kwargs):
        category_menu = ContentCategory.objects.all()
        category_value = super(AudioDermaBlogDetailView,self).get_context_data(*args,**kwargs)
        like_objects = get_object_or_404(BlogPost,id=self.kwargs['pk'])
        like_value = like_objects.BlogPostTotalLikes()
        audio_file = like_objects.speak_content()
        blog_liked = False
        no_dislikes = 0
        if like_objects.Bloglikes.filter(id = self.request.user.id).exists():
            blog_liked = True
        else:
            no_dislikes = no_dislikes + 1
        category_value['category_menu'] = category_menu
        category_value['like_value'] = like_value
        category_value['blog_liked'] = blog_liked
        category_value['no_dislikes'] = no_dislikes
        category_value['audio_file'] = audio_file
        return category_value
    success_url = reverse_lazy('DermaBlogPage')
class AudioDermaBlogDetailViewTwo(DetailView):
    model = BlogPost
    template_name = 'DermaCareApp/DermaBlogAudioReader.html'

    def get_context_data(self,*args,**kwargs):
        category_menu = ContentCategory.objects.all()
        category_value = super(AudioDermaBlogDetailViewTwo,self).get_context_data(*args,**kwargs)
        like_objects = get_object_or_404(BlogPost,id=self.kwargs['pk'])
        like_value = like_objects.BlogPostTotalLikes()
        audio_file = like_objects.speak_subcontent()
        blog_liked = False
        no_dislikes = 0
        if like_objects.Bloglikes.filter(id = self.request.user.id).exists():
            blog_liked = True
        else:
            no_dislikes = no_dislikes + 1
        category_value['category_menu'] = category_menu
        category_value['like_value'] = like_value
        category_value['blog_liked'] = blog_liked
        category_value['no_dislikes'] = no_dislikes
        category_value['audio_file'] = audio_file
        return category_value
    success_url = 'DermaBlogPage'


class UserBlogView(ListView):
    model = BlogPost
    template_name = 'DermaCareApp/UserBlog.html'
    ordering = ['-date_posted']

class AddDermaBlogView(CreateView):
    model = BlogPost
    form_class = DermaBlogPostForm
    template_name = 'DermaCareApp/Add_DermaBlogPost.html'
    # fields = '__all__'

class AddDermaCommentView(CreateView):
    model = BlogComment
    form_class = DermaBlogCommentForm
    template_name = 'DermaCareApp/Add_DermaCommentPost.html'
    def form_valid(self, form):
        form.instance.blogpost_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('DermaBlogPage')

class AddDermaCommentReplyView(CreateView):
    model = Reply
    form_class = DermaBlogReplyForm
    template_name = 'DermaCareApp/Add_Reply.html'

    def form_valid(self, form):
        form.instance.comment_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('DermaBlogPage')


class AddSkinDiseaseCategoryView(CreateView):
    model = ContentCategory
    template_name = 'DermaCareApp/AddSkinDiseaseCategory.html'
    fields = '__all__'
    
class UpdateDermaBlogView(UpdateView):
    model = BlogPost
    template_name = 'DermaCareApp/Update_DermaBlogPost.html'
    # fields = '__all__'
    form_class = UpdateDermaBlogPostForm

class DeleteDermaBlogView(DeleteView):
    model = BlogPost
    template_name = 'DermaCareApp/DeleteDermaBlog.html'
    success_url = reverse_lazy('DermaBlogPage')


def ChatterBotPage(request):
    chatbot = ChatBot('DermaCare Customer Service Bot',
        logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ])
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english',
                  'chatterbot.corpus.english.greetings',
                  'chatterbot.corpus.english.conversations',)
    
    trainer2 = ListTrainer(chatbot)
    trainer2.train([

        "Hi",
        "Hello, Dear user",

        "name",
        "My name is DermaCare Service ChatBot",

        "Help me","What can I help you, the service that I am trained to give are the following: 1), giving service related to account creation",

        "ሰላም",
        "ሰላም ጤና ይስጥልኝ, እባክህ እንዴት ልረዳህ እችላለሁ?",

        "ምን አይነት አገልግሎት መስጠት ትችያለሽ።",
        "እኔ አገልግሎት ለመስጠት የሰለጠንኩት ከድረ-ገጹ ተጠቃሚ ጋር አጠቃላይ ውይይት ማድረግ፣ ለአዲሱ ተጠቃሚ እንዴት አዲስ አካውንት መፍጠር እና ማስተዳደር እንዳለበት እና ከቆዳ እንክብካቤ ጋር የተገናኘ የህክምና መረጃ ማግኘትን ያካትታል።"

        "አዲስ account እንዴት መፍጠር እችላለሁ?",
        "በ DermaCare ድህረ ገጽ ውስጥ፣ በሁለት የተለያዩ መንገዶች account መፍጠር ይችላሉ። የመጀመሪያው መንገድ እንደ ተጠቃሚ ብቻ መለያ መፍጠር ነው። አንድ ተጠቃሚ በድረ-ገጽ ውስጥ ያሉ ብሎጎችን ለማየት፣በኤአይአይ የተጎላበተ የህክምና ምርመራ ለማግኘት፣ከዳርማቶሎጂስቶች እና ከሌሎችም ጋር የህክምና ቀጠሮ የሚያገኙበትን አካል የሚያመለክት ነው። የተጠቃሚ መለያ ለመፍጠር ማድረግ ያለብዎት በድረ-ገጹ የላይኛው ቀኝ ጥግ ላይ የሚገኘውን የተጠቃሚ አዶ ገብተው ጠቅ ያድርጉት። እሱን ሲጫኑ የመግቢያ ሊንኩን የያዘ ሜኑ ንጥል ያሳያል ፣ እሱን ጠቅ ያድርጉ ፣ ወደ መለያ መግቢያ ገጽ ይወስድዎታል ፣ በዚያ ገጽ ውስጥ ይመዝገቡ የሚል አገናኝ አለ ፣ ከዚያ ጠቅ ያድርጉ እና ይጫናል ። ወደ ሚና መምረጫ ገጽ ውሰድ ፣ ከተቆልቋዩ ውስጥ የተጠቃሚ ሚና ምርጫን ምረጥ እና ከዚያ በኋላ የተጠቃሚ ምዝገባ ፎርም ይጠየቃል ፣ ያቀረብከው መረጃ ሁሉ ትክክል ከሆነ መለያ ይፈጥርልሃል። የቆዳ ህክምና ባለሙያን ለመመዝገብ ከፈለጉ ፣ ከላይ ካለው የተለየ ብቸኛው ነገር በ ሚና ምርጫ ገጽ ላይ የቆዳ ህክምና ባለሙያውን ይምረጡ ፣ ከዚያ የቆዳ ህክምና ባለሙያዎች መመዝገቢያ ገጽ ይጠየቃል ፣ ከዚያ ሁሉንም አስፈላጊ መረጃዎች ማከል አለብዎት ። ከላይ ያሉትን ሁሉንም ደረጃዎች በጥንቃቄ ከተከተሉ የሁለቱም መለያ ሊኖርዎት ይገባል::",

        "ለፈጠርኩት አካውንት እንዴት ፕሮፋይል ፒክቸር ይኖረኛል?",
        "እንደ አዲስ ተጠቃሚ ሲመዘገቡ ስርዓቱ ነባሪ የመገለጫ ስዕል ይሰጥዎታል ፣ ግን በእራስዎ ምስል መለወጥ ከፈለጉ ፣ በጎን አሞሌው ላይ ባለው የብሎግ ጣቢያ ላይ ነባሪ አዶውን ጠቅ በማድረግ በቀላሉ የprofile pictureን ማዘመን ይችላሉ።"

        "Eczema ምንድን ነው?",
        "Eczema የሚያቃጥል የቆዳ በሽታ ሲሆን ይህም ማሳከክ፣ ደረቅ ቆዳ፣ ሽፍታ፣ ቅርፊቶች፣ አረፋዎች እና የቆዳ ኢንፌክሽን ያስከትላል።",

        "ምንድን ነው",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",
        
        "መንስኤዎች",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",

        "ዓይነቶች",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",

        "መከላከል",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",

        "መድኃኒት",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",

        "ምን ያህል የተለመደ ነው?",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",
       
        "ዓይነቶች ምን ምን ናቸው?",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",
        
        "በጣም የሚያጠቃው ማንን ነው?",
        "ምን ለማለት እንደፈለጋችሁ፣ ምክንያቱ ለማን እንደሆነ ለመረዳት አልቻልኩም። ምን ለማለት እንደፈለክ በግልፅ በመግለጽ እንዲገባኝ አድርግ።",
        
        "Eczema እንዴት ማከም እችላለሁ?",
        "ለኤክማማ ለማከም የሚከተሉትን የሕክምና ዘዴዎች መጠቀም ይችላሉ-ደረቅ ቆዳ በሚኖርበት ጊዜ ቀኑን ሙሉ ለስላሳ ወይም ስሜታዊ የሆኑ የቆዳ እርጥበቶችን መጠቀም። ገላዎን ከታጠቡ በኋላ ቆዳዎ እርጥብ በሚሆንበት ጊዜ እርጥበትን ይተግብሩ። በአገልግሎት ሰጪዎ እንደታዘዘው እንደ ወቅታዊ ስቴሮይድ ያሉ የአካባቢ መድሃኒቶችን በቆዳዎ ላይ ይተግብሩ።",
        
        "የ Eczema ዋና መንስኤዎች ምንድን ናቸው",
        "Eczema የሚያስከትሉ የተለመዱ ቀስቅሴዎች የሚከተሉትን ያካትታሉ: ደረቅ የአየር ሁኔታ (ዝቅተኛ እርጥበት). ጨርቆች ወይም የልብስ ቁሳቁሶች.ሜካፕ ወይም የቆዳ እንክብካቤ ምርቶች. ጭስ እና ብክለት. ሳሙና እና ሳሙናዎች. ውጥረት ወይም ስሜታዊ ደህንነትዎ። አለርጂ የሆነብህን ነገር መንካት።",

        "የ Eczema ዓይነቶች ምን ምን ናቸው?",
        "በርካታ ዓይነት Eczemaዎች አሉ. እያንዳንዱ አይነት የቆዳዎን ማገጃ ተግባር የሚነኩ ልዩ ቀስቅሴዎች አሉት። Atopic dermatitis, Contact dermatitis, Dyshidrotic eczema, Dyshidrotic eczema, Nummular eczema Seborrheic dermatitis ዋናዎቹ ዓይነቶች ናቸው::",
        
        "Eczema በጣም የሚያጠቃው ማንን ነው?",
        "Eczema በማንኛውም ዕድሜ ላይ በማንኛውም ሰው ላይ ሊደርስ ይችላል. ምልክቶቹ ብዙውን ጊዜ በልጅነት ጊዜ ይታያሉ እና እስከ ጉልምስና ድረስ ይቆያሉ.",

        "Eczema ምን ያህል የተለመደ ነው?",
        "ጨቅላ ህጻናት ለEczema የተጋለጡ ናቸው, እና ከ 10% እስከ 20% የሚሆኑት ይደርስባቸዋል.",

        "Eczemaን እንዴት መከላከል እችላለሁ?", 
        "የEczemaን ወረርሽኞን ለመከላከል ሊወስዷቸው የሚችሏቸው እርምጃዎች አሉ፡ ከነዚህም ውስጥ፡-ቆዳዎን በየጊዜው ወይም ቆዳዎ ሲደርቅ ቆዳዎን ያርቁ. ገላዎን ከታጠቡ ወይም ገላዎን ከታጠቡ በኋላ እርጥበትን ያሽጉ ፣ ወዲያውኑ እርጥበትን በቆዳዎ ላይ ይተግብሩ።ሙቅ ሳይሆን ሙቅ በሆነ ውሃ ገላ መታጠብ ወይም ገላ መታጠብ።እርጥበት ይኑርዎት እና በየቀኑ ቢያንስ ስምንት ብርጭቆ ውሃ ይጠጡ። ውሃ ቆዳዎን እርጥብ ለማድረግ ይረዳል.ከጥጥ እና ከሌሎች የተፈጥሮ ቁሶች የተሰሩ ለስላሳ ልብሶችን ይልበሱ. አዲስ ልብስ ከመልበስዎ በፊት ይታጠቡ። ሱፍ ወይም ሰው ሰራሽ ፋይበርን ያስወግዱ።",
        
        "ለEczema መድኃኒት አለው?",
        "የለም፣ ለEczema መድኃኒት የለውም። ሕክምናዎች አሉ ነገርግን ምንም ዓይነት ሕክምና 100% የሕመም ምልክቶችዎን ሊያስወግድ አይችልም. Eczema ሥር የሰደደ በሽታ ነው, ይህም ማለት በድንገት ሊሄድ እና ሊመለስ ይችላል. ህክምናዎች የማሳከክ እና ደረቅ ቆዳ ምልክቶችን ለመቀነስ በጣም ውጤታማ ናቸው.",
       

        "Melanoma ምንድን ነው?",
        "Melanoma ከፍተኛውን የመሞት እድል ያለው በጣም ወራሪ የቆዳ ካንሰር ነው። ከባድ የቆዳ ካንሰር ቢሆንም፣ ቶሎ ከተያዘ በጣም ይድናል።",

        "Melanoma እንዴት ማከም እችላለሁ?",
        "ለMelanoma ሕክምናዎች;ሜላኖማ ቀዶ ጥገና, ሊምፍዴኔክቶሚ, ሜታስታሴክቶሚ, የታለመ የካንሰር ሕክምና.",
        
        "የ Melanoma ዋና መንስኤዎች ምንድን ናቸው",
        "ለMelanoma ዋነኛው ተጋላጭነት ለፀሀይ ብርሀን በተለይም በወጣትነትዎ ወቅት በፀሀይ ቃጠሎ መጋለጥ እንደሆነ ብዙ ባለሙያዎች ይስማማሉ።",
        
        "Melanoma በጣም የሚያጠቃው ማንን ነው?",
        "Melanoma በማንኛውም ዕድሜ ላይ በማንኛውም ሰው ላይ ሊደርስ ይችላል. ምልክቶቹ ብዙውን ጊዜ በልጅነት ጊዜ ይታያሉ እና እስከ ጉልምስና ድረስ ይቆያሉ.",

        "Melanomaን እንዴት መከላከል እችላለሁ?", 
        "እራስዎን ከመጠን በላይ ከፀሀይ እና ከፀሀይ ቃጠሎዎች በመጠበቅ የሜላኖማ ስጋትዎን ሊቀንሱ ይችላሉ. በተለይ ከጠዋቱ 10 ሰዓት እስከ ምሽቱ 4 ሰዓት ድረስ ፀሐይን ያስወግዱ እና ጥላን ይፈልጉ።የቆዳ አልጋዎችን አይጠቀሙ. በምትኩ የሚረጭ ታን (ኮስሜቲክስ) ይጠቀሙ።በተቻለ መጠን ባርኔጣዎችን ከዳርቻዎች ፣ ከፀሐይ መነፅር ፣ ረጅም-እጅጌ ሸሚዝ እና ሱሪ ይልበሱ።",
        
        "ለMelanoma መድኃኒት አለው?",
        "የ Melanoma ካንሰርን ማዳን ላይቻል ይችላል. በዚህ ሁኔታ የሕክምናዎ ዓላማ ካንሰርን እና ምልክቶቹን መገደብ እና ረጅም ዕድሜ እንዲኖሩ መርዳት ነው።" ,


        "ደህና ነሽ",
        "ደህና ነኝ እግዚአብሄር ይመስገን", 

         "ሃይ",
         "ሀሎ",

         "ስምሽ ማን ነው",
         "ስሜ DermaCare Service ChatBot ነው።",

         "What is your name",
         "My name is DermaCare Service ChatBot",

         "what is eczema",
         "Eczema is a skin condition that causes dry and itchy patches of skin. It's a common condition that isn't contagious"
         
         "what is melanoma",
         "Melanoma is a form of skin cancer that begins in the cells (melanocytes) that control the pigment in your skin.Other names for this cancer include malignant melanoma and cutaneous melanoma.",

         "what is the cause of eczema",
         "The major cause of eczema includes: irritants, environmental factors or allergens , food allergies , certain materials worn next to the skin, and hormonal changes.",

         "How common is eczema?",
         "Eczema is common and affects more than 31 million Americans. Infants are prone to eczema, and 10% to 20% will have it. However, nearly half of all infants diagnosed with eczema outgrow the condition or have significant improvement as they get older.",

         "What are the symptoms of eczema?",
         "Symptoms of eczema include:Dry skin, Itchy skin, Skin rash, Bumps on your skin, Thick, leathery patches of skin, Flaky, scaly or crusty skin, Swelling.", 

         "What does an eczema rash look like?",
         "Eczema can look different on each person diagnosed with the condition. If you have a dark skin tone, an eczema rash can be purple, brown or gray. If you have a light skin tone, an eczema rash can look pink, red or purple.",

         "Where do symptoms of eczema appear on my body?",
         "Symptoms of eczema can show up anywhere on your skin. The most common places where you’ll notice symptoms of eczema include on your:Hands,Neck, Elbows and Ankles",

         "Do eczema hurt",
         "Eczema doesn’t usually cause pain. If you scratch your skin, you could break the surface of your skin and create a sore, which could be painful. Some types of eczema, like contact dermatitis, cause a burning sensation and discomfort.",

        "What causes eczema?",
        "Several factors cause eczema, including:Your immune system, Your genes, Your environment and Emotional triggers",
        
        "How do I get rid of eczema?",
        "Your treatment for eczema is unique to you and what caused your symptoms to flare up. Treatment for eczema could include: Using gentle or sensitive skin moisturizers throughout the day when you have dry skin. Apply moisturizer when your skin is damp after a bath or shower. Apply topical medications to your skin as advised by your provider, like topical steroids.",
        
        "How do I manage my eczema symptoms?",
        "Treating and managing eczema can be difficult if the cause is something you can’t control, like genetics. Fortunately, you may have some influence over your environment and stress levels.",

        "How can I prevent eczema?",
        "There are steps you can take that may prevent eczema flare-ups and outbreaks, including: Moisturize your skin regularly or when your skin becomes dry. Seal in moisture after a bath or shower by immediately applying moisturizer to your skin, Take baths or showers with warm, not hot, water, Stay hydrated and drink at least eight glasses of water each day. Water helps keep your skin moist.",
        "Is there a cure for eczema?",
        "No, there isn’t a cure for eczema. There are treatments available, but no treatment can eliminate your symptoms 100% of the time. Eczema is a chronic condition, which means it can go away and come back unexpectedly.",


         "what is the cause of melanoma",
         "The major cause of melanoma is ultraviolet(UV).It comes from the sun and is used in sunbeds.People with black or brown skin most often get melanoma on the soles of the feet, palms of the hands, or under a nail.",
         
         "How common is melanoma?",
         "Melanoma accounts for only about 1% of all skin cancers, but causes the great majority of skin cancer-related deaths. It’s one of the most common cancers in young people under 30, especially in young women.",

         "Where can I get melanoma on my body?",
         "You can get melanoma on any area of your body. Melanoma can even form on your eyes and internal organs. Men are more prone to develop melanoma on their trunk — often the upper back. Women are more likely to have melanoma on their legs.",

         "What are the signs of melanoma?",
         "Melanoma can appear as moles, scaly patches, open sores or raised bumps.",

         "What causes melanoma?",
         "Most experts agree that a major risk factor for melanoma is overexposure to sunlight, especially sunburns when you are young. Statistics tell us that 86% of melanomas are caused by solar ultraviolet (UV) rays.",

         "How is melanoma diagnosed?",
         "If you have a mole or other spot that looks suspicious, your doctor may remove it and look at it under the microscope to see if it contains cancer cells. This is called a biopsy.After your doctor receives the skin biopsy results showing evidence of melanoma cells, the next step is to determine if the melanoma has spread. This is called staging.",

         "How is melanoma treated?",
         "The major treatments of melanoma include the following major treatments:Melanoma Surgery,Lymphadenectomy, Metastasectomy, Targeted cancer therapy and Radiation Therapy.",

         "Can melanoma be prevented?",
         "You may reduce your risk of melanoma by protecting yourself from excess sun and sunburns.Avoid sun and seek shade, especially between 10 a.m. and 4 p.m. Don’t use tanning beds. Use a spray tan (cosmetic) instead. Whenever possible, wear hats with brims, sunglasses, long-sleeved shirts and pants.",

         "How to prevent melanoma",
         "You may reduce your risk of melanoma by protecting yourself from excess sun and sunburns.Avoid sun and seek shade, especially between 10 a.m. and 4 p.m. Don’t use tanning beds. Use a spray tan (cosmetic) instead. Whenever possible, wear hats with brims, sunglasses, long-sleeved shirts and pants.",

         "what is tinea ring worm",
         "Ringworm is a contagious fungal infection that causes a circular, ring-like pattern on your skin.Ringworm is spread by skin-to-skin contact or by touching an infected animal or object.",

         "What are the service that you can provide?",
         "The service that I am programmed to give or provide includes: giving a breif medical information about the medical condition which relates with dermatology, provide a guidance how to create and manage a new account, and make a general conversation with you.",

         "How to create an account?",
         "In the DermaCare website, you can create an account in two different ways. The first way is to create an account as a user only. It refers to the part where a user can view blogs in a website, get AI-powered medical diagnosis, book medical appointments with dermatologists and more. All you have to do to create a user account is to log in and click on the user icon in the top right corner of the website. A user registration form will be requested, if all the information you provided is correct, an account will be created for you.",

         "what kind of information do you related to skin disease?",
         "I have been trained to give a medical information on 10 skin disease classes. The classes are eczema, melanoma, atopic dermatits, benginin keratosis, basel cell carcinoma, sebohrreotic keratosis, melanocytic nevy, psoriasis, warts molluscum.",
    ])

    return render(request, 'DermaCareApp/customer_service_bot.html')

def UserBlog(request):
    return render(request, "DermaCareApp/UserBlog.html")
def chat(requets):
    return HttpResponse("<h2>Chat Page</h2>")
def contact(request):
    return HttpResponse("<h2>Contact Us Page</h2>")
def registeruser(request):
    return HttpResponse("<h2>Register Page for User")
def registerderma(request):
    return HttpResponse("<h2>Register Page for Derma")
def login(request):
    return HttpResponse("<h2>Log in Page</h2>")
def role(request):
    return HttpResponse("<h2>Role Page</h2>")