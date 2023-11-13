from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, default='avatars/default.jpg', upload_to='avatars')

    def __str__(self):
        return f"{self.user.username} Profile"
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        #now, open the image on this profile instance
        img = Image.open(self.avatar.path)

        #check if image is big enough that we'd want to resize it
        if img and (img.height > 300 or img.width > 300):
            max_output_size = (300, 300)
            img.thumbnail(max_output_size)
            #by saving, we overwrite the large image with the new thumbnail
            img.save(self.avatar.path)

