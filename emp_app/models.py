from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100)  # Corrected spelling
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)  
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)  
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField()
    hire_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
