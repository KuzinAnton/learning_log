from django.db import models

# Create your models here.
class Topic(models.Model):
	"""Тема, уоторую изучает пользователь"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeFieldauto_now_add=True)
	
	def __str__(self):
		"""Возвращает строковое представление модели"""
		return self.text