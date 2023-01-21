from django.shortcuts import render

from croaker.models import Profile


def dashboard(request):
    return render(request, 'croaker/home.html')


def profile_list(request):
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