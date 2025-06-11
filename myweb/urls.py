"""myweb URL Configuration

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
from django.urls import path
from home.views import home_view

from django.conf import settings
from django.conf.urls.static import static
from question import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('yeni/<str:soru>', views.yeni, name='yeni'),

    #path('home', home_view),

    #path('display', views.display_images),

    #path('done', views.done, name ='done'),

    path('', views.info_view, name ='information'),

    path('quiz/body/<str:email>', views.body, name="body"),

    path('quiz/<str:qtype>', views.questions, name='questions'),

    path('result<str:result>', views.tekresult, name = 'results'),

    path('quiz/website/navbar/<str:url>', views.navbar, name="navbar"),

    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)