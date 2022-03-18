from dataclasses import Field
from django.db import models

# Create your models here.
class JobType1(models.Model):
    id= models.AutoField(primary_key=True)
    Category = models.CharField(max_length=256,unique=True)

class JobType2(models.Model):
    id= models.AutoField(primary_key=True)
    Category = models.ForeignKey(JobType1,to_field='Category',db_column='Category',on_delete=models.CASCADE  )
    Subcategory=models.CharField(max_length=256,unique=True)

class States(models.Model):
    id= models.AutoField(primary_key=True)
    State =models.CharField(max_length=256,unique=True)

class CompanyDetails(models.Model):
    id= models.AutoField(primary_key=True)
    Name =models.CharField(max_length=256)
    Field =models.CharField(max_length=256)
    Headquarters =models.CharField(max_length=256)
    Description=models.CharField(max_length=2000)
    class Meta:
        unique_together = ['Name', 'Field']

class Jobs(models.Model):
    id= models.AutoField(primary_key=True)
    Company_id= models.ForeignKey(CompanyDetails,db_column="Company_id",on_delete=models.CASCADE)
    JobPosition =models.CharField(max_length=256)
    Location =models.CharField(max_length=256)
    WorkType=models.CharField(max_length=2000)
    State=models.ForeignKey(States,to_field='State',db_column='State',on_delete=models.CASCADE)
    Subcategory=models.ForeignKey(JobType2,to_field='Subcategory',db_column="Subcategory",on_delete=models.CASCADE)
    class Meta:
        unique_together = ['Company_id', 'JobPosition']