from django.db import models

# Create your models here.
class tEM_Employee(models.Model):
    Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    '''
    DepartmentID = models.IntegerField()
    '''
    DepartmentID = models.ForeignKey('tEM_Department', db_column='DepartmentId', on_delete=models.CASCADE,)
    class Meta:
        db_table = 'tEM_Employee'
    class Meta:
        db_table = 'tEM_Employee'
        verbose_name_plural = 'tEM_Employee'
        ordering = ['Id']
        indexes = [models.Index(fields=['Id'], name='tEM_EmployeeId')]

    def __str__(self):
        return self.FirstName + " " + self.LastName

class tEM_Department(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tEM_Department'
        verbose_name_plural = 'tEM_Department'
        ordering = ['Id']
        unique_together = (('Id', 'Name'),)
        indexes = [models.Index(fields=['Id'], name='tEM_DepartmentId')]

    def __str__(self):
        return self.Name