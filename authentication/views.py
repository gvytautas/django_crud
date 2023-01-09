from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, UpdateUserForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration succeeded. You can login now.')
            return redirect(reverse('index'))
        messages.error(request, 'Form data not valid.')
        return render(request, 'registration/sign_up.html', context={'form': form})
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


def user_account(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_account'))
        return redirect(reverse('user_account'))
    else:
        form = UpdateUserForm(initial={
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })
    return render(request, 'user_account.html', context={'form': form})
