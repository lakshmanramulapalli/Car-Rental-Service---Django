from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import user_login, user_logout, register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('bookings/', include('bookings.urls')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html')),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


