from django.db import models

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
        # `related_name` is used to access the `Profile`s who follow
        # this `Profile`.
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
        return str(self.id) + ' - ' + self.user.username
