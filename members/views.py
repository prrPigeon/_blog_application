from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

"""def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'You Are Successfuly Created Account for {username}!')
			return redirect('blog-home')
	else:
		form = UserCreationForm()
	return render(request, 'members/registration.html', {'form': form})"""

def register_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			"""messages.success(request, f'You Are Successfuly Created Account for {username}!')
			return redirect('blog-home')"""
			messages.success(request, f'Your account has been created for {username} username! You are now able to log in!')
			return redirect('login_page')
	else:
		form = UserRegisterForm()
	return render(request, 'members/registration.html', {'form': form})


@login_required
def profile_view(request):
	if request.method == 'POST':
		user_update_form = UserUpdateForm(request.POST, instance=request.user)
		profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if user_update_form.is_valid() and profile_update_form.is_valid():
			user_update_form.save()
			profile_update_form.save()
			messages.success(request, f"You're successfuly update your account!")
			return redirect('profile')

	else:
		user_update_form = UserUpdateForm(instance=request.user)
		profile_update_form = ProfileUpdateForm(instance=request.user.profile)		

	context = {
				'user_update_form': user_update_form, 
				'profile_update_form': profile_update_form
				}
	return render(request, 'members/profile.html', context)
