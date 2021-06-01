"""
website app views document
"""
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


@login_required
def user_show(request, user_id):

    return render(
        request,
        'user_show.html', {
            'user': User.objects.get(id=user_id)
        })


@login_required
def users(request):
    all_users = User.objects.values()
    return render(
            request,
            'users.html', {
                'users': all_users
            })


@login_required
def register(request):
    """
    Display register user of the site

    Returns:
        template : "registration/register.html"
    """

    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {
                "form": CustomUserCreationForm
            }
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('profile'))

