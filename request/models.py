from django.db import models

# Create your models here.
class Request(models.Model):
    req_id = models.AutoField(primary_key=True)
    hb_id = models.IntegerField()
    blood_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'request'

