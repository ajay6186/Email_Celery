from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)

    def get_full_name(self):
        return F"{self.first_name} {self.last_name}"

    def __str__(self):
        return get_full_name(self)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "User Profile"
