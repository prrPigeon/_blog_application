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
	path('password-reset',
		 authentification_views.PasswordResetView.as_view(template_name='members/password_reset.html'), 
		 name='password_reset'),
	path('password-reset/done/',
		 authentification_views.PasswordResetDoneView.as_view(template_name='members/password_reset_done.html'), 
		 name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/',authentification_views.PasswordResetConfirmView.as_view(
		template_name='members/password_reset_confirm.html'), name='password_reset_confirm'),

	path('password-reset-complete/', authentification_views.PasswordResetCompleteView.as_view(
		template_name='members/password_reset_complete.html'), name='password_reset_complete'),

	path('', include('members.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)