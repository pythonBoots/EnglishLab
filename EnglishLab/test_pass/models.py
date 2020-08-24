from django.db import models

# Create your models here.

# Model for test name and description
class TestWhole(models.Model):
    test_name = models.CharField(max_length=100)
    test_description = models.CharField(max_length=300)

# Model for task with question 
class Task(models.Model):
    testwhole = models.ForeignKey(TestWhole, on_delete=models.CASCADE)
    task_number = models.IntegerField(default=0)
    question_text = models.CharField(max_length=200)
    
# Model for options 
class Option(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)

