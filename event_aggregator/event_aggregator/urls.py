from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

from django.contrib import messages
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static

def logout_and_message(request):
    messages.success(request, "Ai fost delogat cu succes.")
    return auth_views.LogoutView.as_view(next_page='login')(request)

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_and_message, name='logout'),
    path('register/', user_views.register, name='register'),
    path('', include('events.urls')),
    path('api-client/', include('event_client.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)