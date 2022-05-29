from django.db import models

# Create your models here.
class Login(models.Model):
    log_id = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Useername', max_length=30)  # Field name made lowercase.
    password = models.CharField(max_length=30)
    stud_id = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'login'
