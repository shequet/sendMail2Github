"""
website app views document
"""
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


@login_required
def user_show(request, user_id):
    try:
        return render(
            request,
            'user_show.html', {
                'user': User.objects.get(id=user_id)
            })
    except User.DoesNotExist:

        return render(
            request,
            'users.html', {
                'users': User.objects.values(),
                'message': "L'utilisateur n'existe pas"
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
def user_add(request):
    """
    Display register user of the site

    Returns:
        template : "registration/register.html"
    """

    if request.method == "GET":
        return render(
            request, "user_add.html",
            {
                "form": CustomUserCreationForm
            }
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_show', user_id=user.id)
        else:
            return render(
                request, "user_add.html",
                {
                    "form": CustomUserCreationForm,
                    "errors": form.error_messages
                }
            )


@login_required
def user_edit(request, user_id):
    """
    Display register user of the site
    """

    if request.method == "GET":
        return render(
            request, "user_edit.html",
            {
                "form": CustomUserCreationForm(instance=User.objects.get(id=user_id))
            }
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=User.objects.get(id=user_id))

        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()

            return redirect('user_show', user_id=update.id)
        else:
            return render(
                request, "user_edit.html",
                {
                    "form": CustomUserCreationForm(instance=User.objects.get(id=user_id)),
                    "errors": form.error_messages
                }
            )


@permission_required('is_superuser')
def user_delete(request, user_id):
    all_users = User.objects.values()
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return render(
            request,
            'users.html', {
                'users': all_users,
                'message': "L'utilisateur est supprimé"
            })
    except User.DoesNotExist:
        return render(
            request,
            'users.html', {
                'users': all_users,
                'message': "L'utilisateur n'existe pas"
            })
