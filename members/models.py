from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	image = models.ImageField(default='default_pic.jpg', upload_to='profilePictures')

	def __str__(self):
		return f'{self.user.username} Profile Page'


	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		user_image = Image.open(self.image.path)

		if user_image.height > 300 or user_image.width > 300:
			output_size = (300, 300)
			user_image.thumbnail(output_size)
			user_image.save(self.image.path)

	"""def save(self):
		super().save() dobio si type error zbog ovog dela..."""
