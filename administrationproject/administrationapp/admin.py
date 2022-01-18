from django.contrib import admin
from administrationapp.models import Forms #or ,contact
from administrationapp.models import EmployeeDetails

# Register your models here.
class formsAdmin(admin.ModelAdmin):

	list_display=('Name', 'DOB','Gender','Age','Contact','Email','Suggestion')

admin.site.register(Forms,formsAdmin)
admin.site.register(EmployeeDetails)


