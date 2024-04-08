from django.db import models
from django.contrib.auth.models import AbstractUser





# Create your models here.
class CustomUser(AbstractUser):
    USER=(
        (1,'ADMIN'),
        (2, 'ADVOCATE'),
        (3, 'USER'),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Advocate(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    regno = models.CharField(max_length=100, null=True)
    public = models.CharField(max_length=80, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + "" + self.admin.last_name

class Advisor(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + "" + self.admin.last_name

class Users(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + "" + self.admin.last_name


class Case(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    advocate_id = models.ForeignKey(Advocate,null=True, on_delete=models.CASCADE)
    content = models.TextField()
    cost = models.IntegerField(null=True)
    file = models.FileField(upload_to='media/profile_pic', null=True)
    status = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class QndA(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    advisor_id = models.ForeignKey(Advisor, on_delete=models.CASCADE, null=True)
    content =models.TextField()
    reply = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Notifications(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    advocate_id = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    content =models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Report(models.Model):
    case_id=models.ForeignKey(Case,on_delete=models.CASCADE)
    file =models.FileField(upload_to='media/profile_pic')
    comments = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Notification(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content