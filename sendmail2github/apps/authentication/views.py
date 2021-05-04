"""
website app views document
"""

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm


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


@login_required
def profile(request):
    """
    Display user profile of the site

    Returns:
       template : "registration/profile.html"
    """

    return render(request, 'registration/profile.html')
