from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    """
    Model representing a user profile, linked to the User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='default_y57ejb', blank=True)

    def __str__(self):
        """
        String representation of the profile, using the username of the associated user.
        """
        return f'{self.user.username} Profile'
