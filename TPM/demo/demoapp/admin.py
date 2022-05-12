from django.contrib import admin
from demoapp.models import Organisation,Admin,Manager,Department,Employee,Task,Client,Work,UserProfileInfo


admin.site.register(Organisation)
admin.site.register(Admin)
admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Client)
admin.site.register(Work)
admin.site.register(UserProfileInfo)
