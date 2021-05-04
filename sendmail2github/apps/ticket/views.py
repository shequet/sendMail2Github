"""
ticket app views document
"""

from django.shortcuts import render
from github import Github
from django.conf import settings


def repositories_index(request):
    g = Github(base_url="https://api.github.com", login_or_token=settings.GITHUB_TOKEN)
    repositories = g.get_user().get_repos()

    return render(request, 'repositories_index.html', {
        'repositories': repositories,
    })


def repository_tickets(request, repository_id):
    g = Github(base_url="https://api.github.com", login_or_token=settings.GITHUB_TOKEN)
    repo = g.get_repo(repository_id)

    return render(request, 'repository_tickets.html', {
        'repo': repo,
        'issues': {
            'open': repo.get_issues(state='open'),
        }
    })
