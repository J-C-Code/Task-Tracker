from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('TaskTracker.urls')),
    path("register/", user_views.register, name='user-register'),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', user_views.user_logout, name="user-logout"),
    path('profile/', user_views.profile, name='user-profile')
]
