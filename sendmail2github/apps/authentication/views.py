"""
website app views document
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    """
    Display user profile of the site

    Returns:
       template : "registration/profile.html"
    """

    return render(request, 'registration/profile.html')
