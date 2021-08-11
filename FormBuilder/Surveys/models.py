from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# from Users.models import User
# Create your models here.


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self):
        return self.title

class SurveyData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    field1 = models.TextField()
    field2 = models.TextField()
    field3 = models.TextField()
    image = models.ImageField(blank = True)

    survey = models.ForeignKey(Survey,on_delete=CASCADE)
    user= models.ForeignKey(User,on_delete=CASCADE)