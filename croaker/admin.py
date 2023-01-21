from django.contrib import admin
from django.contrib.auth.models import Group

from croaker.models import Profile, Croak


# Unregister the Group model from Django Admin Interface since we aren't
# going to be using it currently.
admin.site.unregister(Group)

# Register the `Profile` model with Django Admin Interface.
admin.site.register(Profile)

# Register the `Croak` model with Django Admin Interface.
admin.site.register(Croak)
