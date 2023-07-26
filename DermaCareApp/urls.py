from django.urls import path
from .views import DermaBlogView,UserBlogView
from .views import AddDermaBlogView
from . import views
from .views import UpdateDermaBlogView,servicehomeview,DeleteDermaBlogView,AddSkinDiseaseCategoryView,FilterBlogPostCategoriesView,BlogLikeView
from .views import DermaBlogDetailView, AddDermaCommentView , AddDermaCommentReplyView, AudioDermaBlogDetailView, AudioDermaBlogDetailViewTwo, request_appointment, ManageAppointmentTemplateView
from .views import adminview, searchview, streamlit_view, ChatterBotPage, get_response
from .feeds import BlogPostFeed
from .views import Download,chatview,chatbot_response,download_atopic_photos,download_basalcell_photos,download_photos,ManageAppointmentTemplateView,BenignKeratosisTemplateView,AtopicDermatisView,GalleryTemplateView,EczemaTemplateView,BasalCellCarcinomaTemplateView,MelanocyticNeviTemplateView,MelanomaTemplateView,PsorasisTemplateView,SeborrheicKeratosisTemplateView,TineaRingwormTemplateView,WartsMolluscumTemplateView
urlpatterns = [
    path('',views.home,name="HomePage"),
    path("Gallery_Page/", GalleryTemplateView.as_view(), name="gallery"),
    path('DermaBlog/',DermaBlogView.as_view(),name = "DermaBlogPage"),
    path('DermaBlogDetail/<int:pk>',DermaBlogDetailView.as_view(),name = "DermaBlogDetailsPage"),
    path('AddDermaBlogPost/',AddDermaBlogView.as_view(),name = "AddDermaBlogPage"),
    path('UpdatePost/<int:pk>',UpdateDermaBlogView.as_view(),name="UpdateDermaBlogView"),
    path('DeletePost/<int:pk>',DeleteDermaBlogView.as_view(),name = "DeleteDermaBlogView"),
    path('AddSkinDiseaseCategory/',AddSkinDiseaseCategoryView.as_view(), name = "AddSkinDiseaseCategoryView"),
    path('FilterPostCatagories/<str:FilterCategory>/',views.FilterBlogPostCategoriesView, name="FilterBlogPostCategory"),
    path('BlogLikes/<int:pk>',views.BlogLikeView, name="BlogLikesPage"),
    path('AddDermaComment/<int:pk>',AddDermaCommentView.as_view(),name="AddDermaBlogCommentView"),
    path('AddReply/<int:pk>',AddDermaCommentReplyView.as_view(),name = "AddReplyToCommentView"),
    path('UserBlogView/',UserBlogView.as_view(),name="UserBlogPage"),
    path('UserBlog/',views.UserBlog,name="UserBlogPage"),
    path('Services/',views.services,name="ServicesPage"),
    path('Chat/',views.chat,name="ChatPage"),
    path('About/',views.about,name="AboutPage"),
    path('RegisterForUser/',views.registeruser,name="RegisterForUserPage"),
    path('RegisterForDerma/',views.registerderma,name="RegisterForDermaPage"),
    path('Login/',views.login,name="LoginPage"),
    path('Role/',views.role,name="RolePage"),
    path('admin/', views.adminview, name="adminpage"),
    path('AudioBlog/<int:pk>', AudioDermaBlogDetailView.as_view(), name = "AudioDermaBlog"), 
    path('AudioBlogPartTwo/<int:pk>',AudioDermaBlogDetailViewTwo.as_view(), name="AudioDermaBlogTwo"),
    path('rss/', BlogPostFeed(), name='blog_rss_feed'),
    path('search_blog/', views.searchview, name='searchviewpage'), 
    path("Contact/", views.request_appointment, name="Contact"),
    path("manage-appointment/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("streamlit_app/", views.streamlit_view, name="streamlit_App_View"),
    path('DermaCareChatBotPage/', views.ChatterBotPage, name='ChatBotPage'),
    path('get-response/', views.get_response, name='get_response'),
    path('service_home/', views.servicehomeview , name="servicehome"),


    path("download_photos/", views.download_photos, name="download_photos"),
    path("download_atopic_photos/", views.download_atopic_photos, name="download_atopic_photos"),
    path("download_basalcell_photos/", views.download_basalcell_photos, name="download_basalcell_photos"),


    path("Atopic/", AtopicDermatisView.as_view(), name="atopic"),
    path("BasalCell/", BasalCellCarcinomaTemplateView.as_view(), name="basal"),
    path("BenignKeratosis/", BenignKeratosisTemplateView.as_view(), name="benign"),
    path("Eczema/", EczemaTemplateView.as_view(), name="eczema"),
    path("Melanocytic/", MelanocyticNeviTemplateView.as_view(), name="melanocytic"),
    path("Melanoma/", MelanomaTemplateView.as_view(), name="melanoma"),
    path("Psorasis/", PsorasisTemplateView.as_view(), name="psorasis"),
    path("SeborrheicKeratosis/", SeborrheicKeratosisTemplateView.as_view(), name="seborrhiec"),
    path("TineaRingworm/", TineaRingwormTemplateView.as_view(), name="tinearing"),
    path("WartsMolluscum/", WartsMolluscumTemplateView.as_view(), name="warts"),
    path("Download/", Download.as_view(), name="download"),
    path('chathome', views.chatview, name='chatview'),
    path('chatbot', views.chatbot_response, name='chatbot_response'),
]
