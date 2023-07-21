from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

class Skill(models.Model):
        name = models.TextField(max_length=20)
        value= models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
        created_on = models.DateTimeField(auto_now=True)


class Experience(models.Model):
        job_possition = models.TextField(max_length= 60)
        starte_date = models.DateField()
        end_date = models.DateField()
        is_current = models.BooleanField()
        address = models.TextField()
        job_description = models.TextField()
        company_name = models.TextField(max_length=40)
        created_on = models.DateTimeField(auto_now=True)



class Education(models.Model):
        university_name = models.TextField()
        start_date = models.DateField()
        end_date = models.DateField(blank = True, null = True)
        is_current = models.BooleanField(null = True)
        grade = models.TextField(max_length=60, blank=True, null=True)
        created_on = models.DateTimeField(auto_now=True)

User= get_user_model()

class PersonalInfo(models.Model):
        phone = models.CharField(max_length=20)
        address = models.TextField(max_length=50)
        age = models.PositiveIntegerField(validators=[MaxValueValidator(90), MinValueValidator(18)], default=18)
        about_me = models.TextField(max_length=300)
        created_on = models.DateTimeField(auto_now=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE)


class  SocialLink(models.Model):
        
        link = models.URLField()
        class_name= models.TextField()
        created_on = models.DateTimeField(auto_now=True)



class Language(models.Model):
        name = models.CharField(max_length=20)
        created_on = models.DateTimeField(auto_now=True)


class Testimonial(models.Model):
        testimonial_name  = models.TextField(max_length= 20)
        testimonial_job_possition = models.TextField(max_length= 50)
        testimonial_feedback = models.TextField(max_length=400)
        testimonial_image = models.ImageField(upload_to='media/')
        created_on = models.DateTimeField(auto_now=True)



