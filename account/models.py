from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    email = models.EmailField(max_length=254, verbose_name='email')
    password = models.IntegerField(verbose_name='password')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'

    def __str__(self):
        return "{}".format(self.name)
