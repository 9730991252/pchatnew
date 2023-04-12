from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

Group_category=[
    ('politic','politic'),
    ('village','village'),
    ('education','education'),

]




class School(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True,blank=True)
    added_by=models.CharField(max_length=100)
    added_date=models.DateTimeField(auto_now_add=True,null=True)
    status=models.IntegerField(default=1)

class College(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True,blank=True)
    added_by=models.CharField(max_length=100)
    added_date=models.DateTimeField(auto_now_add=True,null=True)
    status=models.IntegerField(default=1)



class Group_names(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,choices=Group_category)
    ssc_school=models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    hsc=models.ForeignKey(College,on_delete=models.CASCADE,null=True,blank=True)
    ssc_year=models.CharField(max_length=100,null=True,blank=True)
    status=models.IntegerField(default=1)
    added_date=models.DateTimeField(auto_now_add=True,null=True)
 

class Participants(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    village=models.ForeignKey(Group_names,on_delete=models.CASCADE,null=True,blank=True)
    mobile=models.IntegerField()
    status=models.IntegerField(default=1)

class Chat(models.Model):
    group=models.ForeignKey(Group_names,on_delete=models.CASCADE)
    participant=models.ForeignKey(Participants,on_delete=models.CASCADE)
    msg=RichTextField()
    added_date=models.DateTimeField(auto_now_add=True,null=True)
    status=models.IntegerField(default=1)





class My_group(models.Model):
    group=models.ForeignKey(Group_names,on_delete=models.CASCADE)
    participant=models.ForeignKey(Participants,on_delete=models.CASCADE)
