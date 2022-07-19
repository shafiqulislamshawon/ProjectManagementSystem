from django.db import models


# Create your models here.

class ProjectType(models.Model):
    name = models.CharField(max_length=220, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmployeeList(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Status(models.Model):
    name = models.CharField(max_length=220, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Pms(models.Model):
    unique_id = models.CharField(max_length=220, null=True, blank=True)
    name = models.CharField(max_length=220, null=True, blank=True)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, null=True, blank=True)
    poc = models.ManyToManyField(EmployeeList, related_name='poc')
    team = models.ManyToManyField(EmployeeList, related_name='team')
    start_date = models.DateField()
    estimated_end_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unique_id
