from django.db import models

# Create your models here.

'''
django model field :
- html widget
- validation
- db size
'''
JOB_TYPE =(
    ('Full Time', 'Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model): #table
    title = models.CharField(max_length=100) #colum
    # location = 
    job_type = models.CharField( max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.title
    
    
    
    

class Category(models.Model):
    name = models.CharField(max_length=25)




    def __str__(self):
        return self.name
    

