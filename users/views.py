from django.shortcuts import render, redirect
from .forms import SignUpForm
from .user_form import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})
    
@login_required  
def profile(request):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Setelah berhasil mengupdate, redirect ke halaman profil atau halaman lain
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        if user_profile:
            profile_form = ProfileUpdateForm(instance=user_profile)
        else:
            profile_form = ProfileUpdateForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile
    }

    return render(request, 'users/profile.html', context)