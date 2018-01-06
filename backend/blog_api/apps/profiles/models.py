from django.db import models

from blog_api.apps.core.models import TimestampedModel


class Profile(TimestampedModel):
    # There is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)

    # This is an example of a Many-To-Many relationship where both sides of the
    # relationship are of the same model. In this case, the model is `Profile`.
    # This relationship will be one way. Just because you are following me does
    # not mean that I am following you. This is what `symmetrical=False` does
    # for us.
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
    )

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        """Follow `profile` if we're not already following `profile`."""
        self.follows.add(profile)

    def unfollow(self, profile):
        """Unfollow `profile` if we're already following `profile`."""
        return self.follows.remove(profile)

    def is_following(self, profile):
        """Return True if we're following `profile`; False otherwise."""
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        """Returns True if `profile` is following us; False otherwise."""
        return self.is_followed_by.filter(pk=profile.pk).exists()