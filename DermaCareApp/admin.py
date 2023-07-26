from django.contrib import admin
from .models import LatestNews,OurDermatologists,BlogPost,User,Dermatologist, Patient, ContentCategory, UserProfile
from .models import BlogComment,Logo, Reply , Appointment, DermaCategory, Photo, AtopicDermatitis, BasalCellCarcinoma

admin.site.register(BlogComment)
admin.site.register(LatestNews)
admin.site.register(OurDermatologists)
admin.site.register(BlogPost)
admin.site.register(User)
admin.site.register(Dermatologist)
admin.site.register(Patient)
admin.site.register(ContentCategory)
admin.site.register(UserProfile)
admin.site.register(Logo)
admin.site.register(Reply)
admin.site.register(Appointment)
admin.site.register(DermaCategory)
admin.site.register(Photo)
admin.site.register(AtopicDermatitis)
admin.site.register(BasalCellCarcinoma)



