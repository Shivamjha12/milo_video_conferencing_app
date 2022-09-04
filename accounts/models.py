from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Createuserform(UserCreationForm):
    class Meta:
        models   = User
        fields   = ['username','first name','last name','email','password1','password2']
    def fullname(self):
        fullname = self.first_name + ' ' + self.last_name
        return fullname