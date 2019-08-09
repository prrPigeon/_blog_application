from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.contrib.auth import views as authentification_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
	path('post/new/', PostCreateView.as_view(), name='create-post'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
	path('about/', views.about, name='about-blog'),
	path('login/', authentification_views.LoginView.as_view(template_name='members/login.html'), name='login_page'),
	path('logout/', authentification_views.LogoutView.as_view(template_name='members/logout.html'), name='logout_page'),
	path('', include('members.urls')), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)