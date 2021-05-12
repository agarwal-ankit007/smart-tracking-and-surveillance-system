from django.db import models


class Employee(models.Model):
    Employee_Id = models.CharField(max_length=20, primary_key=True)
    Emplyee_Name = models.CharField(max_length=20)
    Email_Id = models.CharField(max_length=20)
    Contact_No = models.IntegerField()
    Address = models.CharField(max_length=100)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=100)

    # eid=models.ForeignKey(login,on_delete=models.cascade)

    class Meta:
        db_table = "Employee"


class Person_Info(models.Model):
    Missing_Id = models.CharField(max_length=20, primary_key=True)
    Name = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='images/')
    Age = models.IntegerField()
    Email_Id = models.CharField(max_length=20)
    Contact_No = models.IntegerField()
    Address = models.CharField(max_length=100)
    Date_Missing = models.DateField()
    Date_Found = models.DateField()
    Status = models.BooleanField()
    Employee_Id = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "Person_Info"
