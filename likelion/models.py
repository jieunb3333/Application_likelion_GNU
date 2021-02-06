from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    user_grade=models.IntegerField(null=True)
    user_pn=models.CharField(max_length=11)
    user_major=models.CharField(max_length=30)
    user_q1=models.TextField()
    user_q2=models.TextField()
    user_q3=models.TextField()
    user_q4=models.TextField()
    user_pass=models.IntegerField(default=2)
    user_time=models.CharField(max_length=20,default='00:00')
    def __str__(self):
        return self.user_name +'/' + self.user_major

    