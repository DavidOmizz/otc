from django.db import models

class CohortInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    campus = models.CharField(max_length=200,blank=True, null=True)
    niche = models.CharField(max_length=200)  # No choices defined here
    gender = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    student = models.CharField(max_length=20)

    def __str__(self):
        return self.name
