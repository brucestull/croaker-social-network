from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from config.settings.common import AUTH_USER_MODEL


class Profile(models.Model):
    """
    Model for the `Profile` of a `CustomUser`.
    """
    # Use `OneToOneField` to create a one-to-one relationship with the
    # `AUTH_USER_MODEL`. Each user will have only one `Profile` associated
    # with them.
    user = models.OneToOneField(
        AUTH_USER_MODEL,
        # `on_delete` is used to specify what happens to this `Profile`
        # if the specific user `AUTH_USER_MODEL` is deleted.
        on_delete=models.CASCADE,
    )
    bio = models.TextField(
        blank=True,
    )
    location = models.CharField(
        max_length=30,
        blank=True,
    )
    # `Profile`s who this `Profile` follows.
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        # `related_name`: This `Profile` is 'followed_by' the other `Profile`s.
        related_name='followed_by',
        blank=True,
        verbose_name='This user follows',
    )
    # `date_joined` is part of `AbstractUser` model, so we don't need
    # to add it here.

    def __str__(self):
        """
        String representation of a `Profile`.
        """
        return 'Profile: ' + str(self.id) + ' - ' + self.user.username


class Croak(models.Model):
    """
    Model for a `Croak`.
    """
    user = models.ForeignKey(
        # `AUTH_USER_MODEL` is used to specify that each `Croak` is associated
        # with a specific user.
        AUTH_USER_MODEL,
        # `on_delete` is used to specify what happens to this `Croak`
        # if the specific user `AUTH_USER_MODEL` is deleted.
        on_delete=models.DO_NOTHING,
        # A user can have many `Croak`s, so we use `related_name` of `croaks`.
        related_name='croaks',
    )
    tiny_body = models.CharField(
        # Use `max_length` of `143` since a numerical interpretation of `143` can be "I love you".
        max_length=143,
    )
    # `date_created` is automatically set to the current date and time
    # when the `Croak` is created.
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        """
        String representation of a `Croak`.
        """
        return (
            self.user.username
            + ' - '
            + self.date_created.strftime('%Y-%m-%d %H:%M:%S')
            + ' - '
            + self.tiny_body[:21]
            + "..."
        )


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a `Profile` for a `CustomUser` when the `CustomUser` is created.
    """
    if created:
        # Create a new profile for the user.
        user_profile = Profile(user=instance)
        # Save the newe profile to the database.
        user_profile.save()
        # Add the user's profile to the list of profiles they follow.
        user_profile.follows.add(instance.profile)
        # Save changes to the profile to the database.
        user_profile.save()