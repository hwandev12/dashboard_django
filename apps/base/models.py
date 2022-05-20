from django.db import models


class HomeSliders(models.Model):
    class Meta:
        verbose_name = 'Home Slider'
        verbose_name_plural = 'Home Sliders'

    slider_text = models.CharField(max_length=101)

    def __str__(self):
        return self.slider_text

