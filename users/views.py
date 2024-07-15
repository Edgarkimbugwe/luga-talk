from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from luga.models import Comment
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse


def register(request):
    """
    View function to handle user registration.

    If request method is POST, processes the registration form.
    If form is valid, creates a new user account and redirects to login page with success message.
    If request method is GET, renders the registration form.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Welcome { username }! Your account was created '
                f'successfully! Please log in!'
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    View function to display and handle user profile update.

    If request method is POST, processes user and profile update forms.
    If forms are valid, updates the user and profile information and displays success message.
    If request method is GET, renders the user profile update form.
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            # Set the success message
            messages.success(
                request, 'Your account has successfully been updated!')

            # Redirect to the profile page
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def delete_account(request):
    """
    View function to handle user account deletion.

    If request method is POST, deletes the user account and associated comments.
    Redirects to home page after deletion with success message.
    If request method is GET, renders the confirmation page for account deletion.
    """
    if request.method == 'POST':
        user = request.user

        # Delete associated comments
        Comment.objects.filter(author=user).delete()

        # Delete the user account
        user.delete()

        # Logout the user after account deletion (optional)
        logout(request)

        messages.success(
            request, 'Your account has been deleted successfully.')
        return redirect('home')

    return render(
        request, 'users/delete_account.html', {'user': request.user})
