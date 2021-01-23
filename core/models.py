from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext, gettext_lazy as _

# Create your models here.
class User(AbstractUser):
	money = models.SmallIntegerField(default=0,verbose_name=_('Bill'))


class Artifact(models.Model):
	name = models.CharField(max_length=70, verbose_name=_('Artifact name'))
	price = models.PositiveSmallIntegerField(verbose_name=_('Artifact price'))
	image = models.ImageField(upload_to='img', verbose_name=_('Artifact picture'))
	description = models.TextField(verbose_name=_('Artifact description'), blank=True)

	def __str__(self):
		return self.name