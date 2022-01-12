from django.contrib import admin
from .models import Contact,Branch,Teacher

class ContactAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "number",
        "email",
        "message",
        "created_date"
    )
    list_filter=("name",)
    search_fields=("name__startswith",)
    
class TeacherAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "email",
        "department",
        "created_date"
    )
    list_filter=("name",)
    search_fields=("name__startswith",)
    
class BranchAdmin(admin.ModelAdmin):
    list_display=(
        "branch",
        "created_date"
    )
    list_filter=("branch",)
    search_fields=("branch__startswith",)



# Register your models here.

admin.site.register(Contact,ContactAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Teacher,TeacherAdmin)
