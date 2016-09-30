from django.db import models


# Create your models here.

class HP(models.Model):
    name = models.CharField(default='', max_length=50)
    blood = models.IntegerField(default=50, max_length=100)
    add_time = models.DateField(auto_now_add=True)
    change_time = models.DateField(auto_now=True)


class Excle(models.Model):
    name = models.CharField(max_length=10)
    excle = models.FileField(upload_to='%Y/%m/%d/')
    add_time = models.DateField(auto_now=True)


class Buff(models.Model):
    DeBuff = (
        ('Level1', (
            ('Duty_Impact', 'Impact on duty'),
            ('Work_Mistake', 'Mistake in work'),
            ('Work_Order_Timeout', 'Work order processing timeout'),
            ('Private_Work_Mistake', 'Private work mistake'),
            ('About_Sing_In', 'No sing in'),
            ('Other', 'Other'),
        ),
         ),
        ('Level2', (
            ('Not_Answer_The_Phone', 'Not answer the phone'),
            ('User_Complaints', 'Errors were complaints'),
            ('SMS_did_not_reply', 'SMS did not reply'),
            ('Absenteeism', 'Absenteeism'),
            ('Skill_points_fail', 'Skill points fail'),
            ('Unauthorized_information', 'Unauthorized dissemination of information'),
            ('Ignore_router', 'Ignore the router'),
            ('Attack_network', 'Attack network'),
            ('Incorrect_use_router', 'Incorrect use of the router'),
            ('Negative_attitude', 'Negative attitude'),
            ('Leak_secrets', 'Leak secrets'),
            ('Workers_complaints', 'Workers complaints'),
            ('Other', 'Other')
        )
         ),
        ('Lever3', (
            ('Cognitive_confusion', 'Cognitive confusion'),
            ('Leaking_private_phone_number', 'Leaking  private phone number'),
            ('Lending_work_permit', 'Lending work permit'),
            ('Lost_work_permit', 'Lost work permit'),
            ('Propaganda_routing', 'Propaganda_routing'),
            ('Illegal_use_IP', 'Illegal use IP'),
            ('Split', 'Split'),
            ('Other', 'Other')
        )
         )
    )
