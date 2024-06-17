from django.db import models

class Admission(models.Model):
    institute = models.CharField(max_length=255)
    academic_program_name = models.CharField(max_length=255)
    seat_type = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, null=True)
    opening_rank = models.IntegerField()
    closing_rank = models.IntegerField()
    year = models.IntegerField()
    round = models.IntegerField()
    has_p = models.BooleanField()
    
    def __str__(self):
        return f"{self.institute} - {self.academic_program_name}"


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
