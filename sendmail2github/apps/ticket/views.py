"""
ticket app views document
"""

from django.shortcuts import render
from github import Github
from django.conf import settings

def tickets(request):
    g = Github(base_url="https://api.github.com", login_or_token=settings.GITHUB_TOKEN)
    repo = g.get_repo(settings.GITHUB_REPO)

    return render(request, 'repository_tickets.html', {
        'repo': repo,
        'labels': repo.get_labels(),
        'assignees': repo.get_assignees(),
        'issues': {
            'open': repo.get_issues(state='open'),
        }
    })
