from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full T ime' , 'Full Time'),
    ('Part Time' , 'Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100)
    # location =
    jop_type = models.CharField(max_length=15, choices=JOB_TYPE)
    describtion = models.TextField(max_length=1000 , default='')
    publish_dt = models.DateTimeField(auto_now=False, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name   
        