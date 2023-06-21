from django.db import models

# Create your models here.
#creating to_do models

class to_do(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    due_date=models.DateField(null=True)
    tag=models.CharField(max_length=40,null=True)
    status=models.CharField(max_length=10,
                            choices=(('OPEN','OPEN'),('WORKING','WORKING'),('DONE','DONE'),('OVERDUE','OVERDUE')))
    Timestamp=models.DateTimeField(auto_now=True)