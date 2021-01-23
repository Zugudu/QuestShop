from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	money = models.SmallIntegerField(default=0,verbose_name='Рахунок')


class Artifact(models.Model):
	name = models.CharField(max_length=70, verbose_name='Назва артефакту')
	price = models.PositiveSmallIntegerField(verbose_name='Ціна артефакту')
	image = models.ImageField(upload_to='img', verbose_name='Світлина артефакту')
	description = models.TextField(verbose_name='Опис артефакту', blank=True)

	def __str__(self):
		return self.name