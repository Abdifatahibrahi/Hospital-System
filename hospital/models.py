from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.mobile} {self.special}"

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    mobile = models.IntegerField(null=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name}, {self.patient.name}"


