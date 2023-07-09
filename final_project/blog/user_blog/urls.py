from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('create/', views.createBlog, name='create'),
    path('blog-detail/<str:pk>/', views.detail_view, name='blog-detail'),
    path('blog/<str:pk>/update/', views.update_view, name='blog-update'),
    path('blog/<str:pk>/delete/', views.delete_view, name='blog-delete'),
    path('register/', views.UserRegister, name= 'register'),
    path('create/login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('search', views.search, name='search')
    
    # path('login/google/', views.google_login, name='google_login'),
    # path('login/google/callback/', views.google_callback, name='google_callback'),
    # path('profile/<str:pk>/', views.profile, name = 'profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)