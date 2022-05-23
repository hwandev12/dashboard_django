from PIL import Image
from django.db import models
from apps.authentication.models import User


# make profile section here
class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)

    avatar = models.ImageField(default='redmi.jpg')
    bio = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username


# create home sliders model
class HomeSliders(models.Model):
    class Meta:
        verbose_name = 'Home Slider'
        verbose_name_plural = 'Home Sliders'

    slider_text = models.CharField(max_length=101)

    def __str__(self):
        return self.slider_text


# create fashion cards
class FashionCards(models.Model):

    class Meta:
        verbose_name = 'Fashion Card'
        verbose_name_plural = 'Fashion Cards'

    image = models.ImageField()
    phone_type = models.CharField(max_length=90)
    price = models.IntegerField(default=50)

    def __str__(self):
        return self.phone_type


# create phone back covers
class PhoneBackCovers(models.Model):

    class Meta:
        verbose_name = 'Phone Back Cover'
        verbose_name_plural = 'Phone Back Covers'

    cover_name = models.CharField(max_length=100)
    cover_price = models.IntegerField(default=5)
    cover_image = models.ImageField()

    def __str__(self):
        return self.cover_name


# create phone accessories
class PhoneAccessories(models.Model):

    class Meta:
        verbose_name = 'Phone Accessories'
        verbose_name_plural = 'Phone Accessories'

    accessories_name = models.CharField(max_length=100)
    accessories_price = models.IntegerField(default=4)
    accessories_image = models.ImageField()

    def __str__(self):
        return self.accessories_name