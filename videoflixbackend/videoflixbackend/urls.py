"""videoflixbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from videostreamApp.views import UserRegistrationView,loginView
from videostreamApp.views import EmailVerificationView,VideoView
from videostreamApp.views import VideoTemplateView
from django.conf import settings
from django.conf.urls.static import static
#from videostreamApp.views import export_video_json
from videostreamApp.views import export_videos_view,import_videos_view
from videostreamApp.views import VideoDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view()),
    path('login/', loginView.as_view()),
    path('videotemplate/', VideoTemplateView.as_view()),
    path('videos/', VideoView.as_view()),
    path('api/videostreamApp/', include('authemail.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('verify/', EmailVerificationView.as_view(), name='email_verification'),
    path('django_/', include('django_rq.urls')),
    path('import/',import_videos_view.as_view(), name='import_videos'),
    path('save/',export_videos_view, name='export_videos'),
    path('videos/<int:pk>/', VideoDetailView.as_view()),

    ##path('verify/<str:code>/', EmailVerificationView.as_view(), name='email_verification_with_code'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.BACKUP_URL, document_root=settings.BACKUP_ROOT)


