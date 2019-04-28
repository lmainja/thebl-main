   
from django.contrib import admin
from django.urls import path, include
from posts import views
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from controlcenter.views import controlcenter
from tinymce import HTMLField

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),
    path('success/', users_views.successView, name='success'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    #path('contact/', contact_views, name='contactus'),
    path('users/', include('users.urls')),
    path('', include('posts.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
