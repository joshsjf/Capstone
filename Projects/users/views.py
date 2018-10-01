from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm, ProfileRegistrationForm


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileRegistrationForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            # user.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, "Your account has been created! You are now able to login.")
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileRegistrationForm()
    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})


@login_required
def profile(request):
    if request.method  == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) 
    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
