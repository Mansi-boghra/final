from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Notice)
class NoticeModel(admin.ModelAdmin):
    list_display = ['send_by','rec_by','subject','des','created_at']

@admin.register(Complain)
class ComplainModel(admin.ModelAdmin):
    list_display = ['complain_by','solve_by','subject','des','status','created_at','solved_at']

@admin.register(Maintenance)
class MaintenanceModel(admin.ModelAdmin):
    list_display = ['pay_by','amount','month','pay_date','verify']

# admin.site.register(ReqEvent)
@admin.register(ReqEvent)
class ReqEventModel(admin.ModelAdmin):
    list_display = ['req_by','title','des','event_at','req_at','status','action','ap_by','ap_at']


