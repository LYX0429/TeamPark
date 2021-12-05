from django.db import models

# Create your models here.



class Doctor(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name