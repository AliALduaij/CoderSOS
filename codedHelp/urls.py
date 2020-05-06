"""codedHelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from codedHelpApp.views import projectListView, requestListView, projectDetailView, requestDetailView, projectCreateView, requestCreateView, UserLoginAPIView, projectUpdateView, projectDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('project/list/', projectListView.as_view(), name='projectlist'),
    path('project/detail/<int:object_id>/',
         projectDetailView.as_view(), name='projectdetail'),
    path('project/create/', projectCreateView.as_view(), name='projectcreate'),
    path('project/update/<int:object_id>/',
         projectUpdateView.as_view(), name='projectupdate'),
    path('project/delete/<int:object_id>/',
         projectDeleteView.as_view(), name='projectdelete'),

    path('request/list/', requestListView.as_view(), name='requestlist'),
    path('request/detail/<int:object_id>/',
         requestDetailView.as_view(), name='requestdetail'),
    path('request/create/', requestCreateView.as_view(), name='requestcreate'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),




]
