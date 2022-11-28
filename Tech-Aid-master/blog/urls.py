from django.urls import path
from . import views
from .views import (
    postblogListView,
    postblogDetailView,
    postblogCreateView,
    postblogUpdateView,
    postblogDeleteView,
    userpostblogListView,
)
from users import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages


urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('',postblogListView.as_view(),name="blog-home"),
    path('user/<str:username>',userpostblogListView.as_view(),name="user-posts"),
    path('post/<int:pk>/',postblogDetailView.as_view(),name="blog-content"),
    path('post/new/',postblogCreateView.as_view(),name="blog-create"),
    path('post/<int:pk>/update/',postblogUpdateView.as_view(),name="blog-update"),
    path('post/<int:pk>/delete/',postblogDeleteView.as_view(),name="blog-delete"),
    path('about/', views.about, name="blog-about"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    path('register/', user_view.register, name="user-register"),
    path('profile/', user_view.profile, name="user-profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

