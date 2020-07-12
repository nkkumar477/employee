from django.db import models


CANDIDATE_STATUS = (
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),

    )

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    picture = models.FileField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=CANDIDATE_STATUS)

    class Meta:
        db_table = "employee"
