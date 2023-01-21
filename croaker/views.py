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
    profile = Profile.objects.get(pk=pk)
    return render(
        request,
        'croaker/profile_detail.html',
        {'profile': profile}
    )
