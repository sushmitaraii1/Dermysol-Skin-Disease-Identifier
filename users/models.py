from django.db import models

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    service = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    note = models.TextField()

    class Meta:
        verbose_name_plural = "Appointment"

    def __str__(self):
        return self.name + "-" + self.email

    models.CharField(max_length=200)


class Disease(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name



