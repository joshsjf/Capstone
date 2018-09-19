from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for {}!".format(username))
            return redirect('sites-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
