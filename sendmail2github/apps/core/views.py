"""
website app views document
"""
from django.shortcuts import render


def home(request):
    """
    Display the index of the site

    Returns:
        template : "home.html"
    """

    return render(request, 'home.html',)
