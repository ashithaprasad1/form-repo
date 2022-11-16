from django.contrib import admin
from myapp.models import Employee 
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    l=['eid','ename','email','edoj','edesig','eexp','ecompany','esal']
admin.site.register(Employee,EmployeeAdmin)