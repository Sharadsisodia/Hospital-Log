"""
URL configuration for loginform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from loginform import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.logIn,name="LogIn"),
    path('signUp',views.signUp,name="SignUp"),
    path('signupComp',views.signupComp,name="signupComp"),
    path('loginPage',views.loginpage,name="loginPage"),
    path('base',views.base,name="base"),  
    path('mypost/',views.myPost,name="myPost"),
    path('postlist',views.postList,name="postlist"),
    path('createpost',views.createPost,name="createPost"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout_view,name="LogOut"),
    path('mentalhealth/',views.mentalhealth,name="mentalhealth"),
    path('heart/',views.heart,name="heart"),
    path('covid/',views.covid,name="covid"),
    path('immune/',views.immune,name="immune"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)