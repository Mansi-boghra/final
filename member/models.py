from django.db import models
from secratory.models import *

# Create your models here.

class Notice(models.Model):
    
    send_by = models.ForeignKey(AdminSec,on_delete=models.CASCADE)
    rec_by = models.ForeignKey(Member,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Complain(models.Model):

    complain_by = models.ForeignKey(Member,on_delete=models.CASCADE)
    solve_by = models.ForeignKey(AdminSec,on_delete=models.CASCADE,null=True,blank=True)
    subject = models.CharField(max_length=80)
    des = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    solved_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.subject + '  ' + self.complain_by.fname


class Maintenance(models.Model):
    
    pay_by = models.ForeignKey(Member,on_delete=models.CASCADE)
    amount = models.IntegerField()
    month = models.DateField()
    pay_date = models.DateTimeField(auto_now_add=True)
    pay_id = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.pay_by.fname + ' >> ' + str(self.month)


class ReqEvent(models.Model):

    req_by = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=50)
    des = models.TextField()
    event_at = models.DateField()
    pic = models.FileField(upload_to='Request Event',null=True,blank=True)
    req_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    action = models.BooleanField(default=False)
    ap_by = models.ForeignKey(AdminSec,on_delete=models.SET_NULL, null=True,blank=True)
    ap_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title + "  >  " + self.req_by.fname + "  " + self.req_by.lname