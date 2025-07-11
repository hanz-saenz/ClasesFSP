"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView
from usuario.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    #renderizar urls de productos a la app de productos
    path('productos/', include('productos.urls')),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    #renderizar urls de usuario a la app de usuario
    path('usuario/', include('usuario.urls')),
    #ursl de login
    path('login-class/', LoginView.as_view(template_name='usuarios/login.html'), name='login-class'),
    #url de logout
    path('logout-class/', LogoutView.as_view(next_page='login'), name='logout-class'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
