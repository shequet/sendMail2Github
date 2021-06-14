"""
website authentication views document
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    """
    Display profile
    """

    return render(request, 'registration/profile.html')
