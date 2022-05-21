from django.db import models


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

