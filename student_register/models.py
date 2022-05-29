from django.db import models

# Create your models here.
class StudentRegister(models.Model):
    stud_id = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Username', max_length=30)  # Field name made lowercase.
    password = models.CharField(max_length=30)
    full_name = models.CharField(db_column='full name', max_length=50)  # Field renamed to remove unsuitable characters.
    email_id = models.CharField(db_column='email id', max_length=30)  # Field renamed to remove unsuitable characters.
    course_name = models.CharField(db_column='course name', max_length=30)  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=15)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    phone_no = models.CharField(db_column='phone no', max_length=12)  # Field renamed to remove unsuitable characters.
    whatsapp_no = models.CharField(db_column='whatsapp  no', max_length=12)  # Field renamed to remove unsuitable characters.
    blood_type = models.CharField(db_column='blood type', max_length=5)  # Field renamed to remove unsuitable characters.
    weight = models.IntegerField()
    disease = models.CharField(max_length=30)
    last_date = models.DateField()

    # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'student_register'


