from django.db import models


class DashboardTopCards(models.Model):
    
    class Meta:
        verbose_name = 'Dashboard Top'
        verbose_name_plural = 'Dashboard Top Cards'

    main_theme = models.CharField(max_length=100)
    money = models.FloatField(default=100)
    users = models.FloatField(default=100)
    new_clients = models.FloatField(default=100)
    sales = models.FloatField(default=100)

    def __str__(self):
        return self.main_theme
