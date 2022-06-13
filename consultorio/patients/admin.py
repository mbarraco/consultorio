from django.contrib import admin
from django.urls import reverse
from django.utils.html import mark_safe # Newer versions

from .models import Appointment, HealthCoverage, Patient, Referent


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "date", "summary")


@admin.register(HealthCoverage)
class HealthCoverageAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('surname', "name", "referent_", "health_coverage")

    # Add it to the details view:
    referent_ = ('referent_',)

    def referent_(self, obj):
        link=reverse("admin:patients_referent_change", args=[obj.referent.id]) 
        return mark_safe(f"<a href='{link}'>{obj.referent}</a>")

    referent_.allow_tags=True

@admin.register(Referent)
class ReferentAdmin(admin.ModelAdmin):
    pass


