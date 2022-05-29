from django.db import models

# Create your models here.
class BloodType(models.Model):
    blood_id = models.AutoField(primary_key=True)
    blood_type = models.CharField(db_column='blood type', max_length=5)  # Field renamed to remove unsuitable characters.
    stud_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blood type'
