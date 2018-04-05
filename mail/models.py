from django.db import models


class Person(models.Model):
    name = models.CharField("ФИО", max_length=128)
    age = models.IntegerField("Возраст")
    email = models.EmailField(max_length=128)
