from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Pms)
admin.site.register(Status)
admin.site.register(EmployeeList)
admin.site.register(ProjectType)
