from django.shortcuts import render

from croaker.models import Profile


def dashboard(request):
    """
    Dashboard view for the Croaker app.
    """
    return render(request, 'croaker/home.html')


def profile_list(request):
    """
    List view for the `Profile` model.
    """
    # Get all the `Profile` objects from the database.
    # profiles = Profile.objects.all()
    # Get all the `Profile` objects from the database except the one
    # for current user.
    profiles = Profile.objects.exclude(user=request.user)
    return render(
        request,
        'croaker/profile_list.html',
        {'profiles': profiles}
    )


def profile_detail(request, pk):
    """
    Detail view for the `Profile` model.
    """
    # Check if user has a `Profile` object:
    if not hasattr(request.user, 'profile'):
        # If not, create one.
        new_profile = Profile.objects.create(user=request.user)

    # Get the requested `Profile` object from the database.
    profile = Profile.objects.get(pk=pk)
    # If the user clicked the `Follow` or `Unfollow` button:
    if request.method == "POST":
        # Get the `Profile` of the current user (`request.user.profile`).
        current_user_profile = request.user.profile
        # Get the data from the form.
        data = request.POST
        # Get the value of the `follow` key from the form data.
        action = data.get('follow')
        # If the value of the `follow` key is `follow`:
        if action == 'follow':
            # Add the `Profile` of the user who was clicked on to `follows`.
            current_user_profile.follows.add(profile)
        # If the value of the `follow` key is `unfollow`:
        elif action == 'unfollow':
            # Remove the `Profile` of the user who was clicked on from `follows`.
            current_user_profile.follows.remove(profile)
        # Save changes to the `Profile` of the current user to the database.
        current_user_profile.save()

    return render(
        request,
        'croaker/profile_detail.html',
        {'profile': profile}
    )
