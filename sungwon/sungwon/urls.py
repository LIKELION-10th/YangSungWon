from django.contrib import admin
from django.urls import path
from myapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first, name='home'),
    path('hobby/',views.hobby, name='hobby'),
    path('favplace/',views.favplace, name='favplace'),
    path('favmusic/',views.favmusic, name='favmusic'),
    path('pic/',views.pic, name='pic'),
    path('profile/',views.profile, name='profile'),
    path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    #path('login/',accounts_views.login, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)