from django.db import models

# Create your models here.
class Notification(models.Model):
    not_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=50)
    blood_id = models.IntegerField()
    stud_id = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'notification'
