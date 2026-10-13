from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=300)
    bio = models.TextField(default='')
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    blocked = models.BooleanField(default=False)
    circle_image = models.ImageField(upload_to='User/circle/', blank=True, null=True)
    rectangle_image = models.ImageField(upload_to='User/rectangle/', blank=True, null=True)