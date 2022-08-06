from django.db import models

# Create your models here.

contectStatusChoice = ((1,"Active"),(2,"Done"))
class Contect(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    subject = models.TextField()
    message = models.TextField()
    status = models.IntegerField(choices=contectStatusChoice, default=1)

    def __str__(self):
        return str(self.id)+" "+(self.email)+" "+(self.subject)