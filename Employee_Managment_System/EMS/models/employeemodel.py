from django.db import models
from django.db import transaction
from datetime import datetime
from django.http import HttpResponseRedirect


# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    dob=models.DateField()
    address=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    managerName=models.CharField(max_length=30,null=True)
    managerId = models.CharField(max_length=20, null=True)
    joinDate=models.DateField(null=True)
    salary=models.IntegerField(null=True, default=0)
    leave=models.IntegerField(null=True, default=0)
    qualification=models.CharField(max_length=30)
    activation_Date = models.DateTimeField(null=True)
    deactivation_Date = models.DateTimeField(null=True)
    account = models.CharField(max_length=20, default="Deactive")
    emailId=models.EmailField()
    password=models.CharField(max_length=20)
    resume = models.FileField(upload_to='documents', null=True)
    image =models.ImageField(upload_to='images/', null=True)
    empCode = models.CharField(primary_key=True, editable=False, max_length=10, unique=True,default="None")

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.empCode == "None":
                last_employee = Employee.objects.select_for_update().order_by('-empCode').first()
                if last_employee:
                    last_number = int(last_employee.empCode[3:])  # Extract the number from the last empCode
                    no = last_number + 1
                else:
                    no = 1
                self.empCode = "{}{:03}".format('EMP', no)
            super().save(*args, **kwargs)
            
class employeeDailyWork(models.Model):
    id = models.AutoField(primary_key=True)
    employeeId = models.CharField(max_length=20)
    employeeName = models.CharField(max_length=20, null=True)
    managerId = models.CharField(max_length=20)
    clientId = models.IntegerField(null=True)
    workDescription = models.CharField(max_length=40,null=True)
    loginTime = models.DateTimeField()
    loginHour = models.TimeField(null=True)
    logoutTime = models.DateTimeField(null=True)
    logoutHour = models.TimeField(null=True)
    date = models.DateField(null=True)
    projectId = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
