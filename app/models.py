from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    gpa = models.IntegerField()
    
    def __str__(self):
        return self.fname
