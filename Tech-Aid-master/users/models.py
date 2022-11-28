from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default="default.jpg", upload_to='profile_pics', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        
        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            dimensions=(300,300)
            img.thumbnail(dimensions)
            img.save(self.image.path)    
