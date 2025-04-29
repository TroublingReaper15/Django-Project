"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home1/<int:pk>',views.home1,name='home1'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('registration/',views.registration,name='registration'),
    path('data/',views.register, name='data'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dash/<int:pk>',views.dash,name='dash'),
    path('query/<int:pk>',views.query,name='query'),
    path('querydata/<int:pk>',views.querydata,name='querydata'),
    path('data/<int:pk>',views.data,name='data'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('search/<int:pk>',views.search,name='search'),
    path('update/<int:pk>',views.update,name='update'),
    path('admin_data/',views.admin_data,name='admin_data'),
    path('admin_email/',views.admin_email,name='admin_email'),
    path('admin_query/',views.admin_query,name='admin_query'),
]
