from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300, null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300, null=True)
    userpic = models.FileField(null=True)
    idpic = models.FileField(null=True)
    aboutme = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=20, null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=300, null=True)
    updationdate = models.DateField(null=True)
    def __str__(self):
        return self.user.username


class DonationArea(models.Model):
    areaname = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=300, null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.areaname


class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donationname = models.CharField(max_length=100, null=True)
    donationpic = models.FileField(null=True)
    collectionloc = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=50, null=True)
    donationdate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    adminremark = models.CharField(max_length=300, null=True, blank=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, blank=True)
    donationarea = models.ForeignKey(DonationArea, on_delete=models.CASCADE, null=True, blank=True)
    volunteerremark = models.CharField(max_length=300, null=True, blank=True)
    updationdate = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.donationname


class Gallery(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.donation.donationname

class Orphange(models.Model):
    lastName = models.CharField(max_length=50, null=True, blank=True)
    firstName = models.CharField(max_length=50)
    contact = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=50)
    orphanageImage = models.FileField(null=True)
    pwd = models.CharField(max_length=20)
    ownerImage = models.FileField(null=True)
    address = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.firstName



class ContactUs(models.Model):
    lastName = models.CharField(max_length=50, null=True, blank=True)
    firstName = models.CharField(max_length=50)
    contact = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return str(self.contact)









