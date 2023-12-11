# myapp/urls.py
from django.urls import path
from django.conf.urls.static import static
from user_authenticate import settings
from .views import *

urlpatterns = [
    # Other URL patterns
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('blog_posts_list/', blog_posts_list, name='blog_posts_list'),
    path('logout/', user_logout,name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)