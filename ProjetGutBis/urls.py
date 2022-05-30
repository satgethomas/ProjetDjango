"""ProjetGutBis URL Configuration

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
from lycee import views
from lycee.views import StudentCreateView, PresenceCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lycee/', views.index, name='index'),
    path('lycee/<int:cursus_id>', views.detail, name='detail'),
    path('lycee/student/<int:student_id>', views.detail_student,
    name='detail_student'),
    path('lycee/student/create', StudentCreateView.as_view(), name='create_student'),
    path('lycee/cursuscall/<int:cursus_id>', views.cursuscall, name='cursuscall'),
    path('lycee/student/update/<int:student_id>', views.update_student, name='update_student'),
    path('lycee/presence/create', PresenceCreateView.as_view(), name='create_presence'),
    path('lycee/presence/<int:presence_id>', views.detail_presence, name='detail_presence'),
    path('lycee/presence/update/<int:presence_id>', views.update_presence, name='update_presence'),
    path('lycee/presence/', views.detail_all_presence, name='detail_all_presence'),

]
