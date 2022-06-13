from phonenumber_field.modelfields import PhoneNumberField

from django.conf import settings
from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import CITextField


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            abstract = True


class HealthCoverage(Base):
    name = CITextField(max_length=20, blank=False, null=False, unique=True)
    plan_id = CITextField(max_length=20, blank=False, null=False, unique=False)

    def __str__(self):
        return self.name + " " + self.plan_id
    
    class Meta:
        unique_together = ('name', 'plan_id')


class Referent(Base):
    name = models.CharField(max_length=20, blank=False, null=False)
    surname = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=20)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.name.title() + " " + self.surname.title()


class Patient(Base):
    name = models.CharField(max_length=20, blank=False, null=False)
    surname = models.CharField(max_length=20, blank=False, null=False)

    health_coverage = models.ForeignKey(HealthCoverage, on_delete=models.SET_NULL, null=True)
    referent = models.ForeignKey(Referent, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.name.title() + " " + self.surname.title()


class Appointment(Base):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=False, null=False)
    summary = models.CharField(max_length=20, blank=False, null=False)
    notes =  models.TextField(max_length=400, blank=True, null=True)  

    def __str__(self):
        return f"{self.patient}'s appointment"

