from django.contrib import admin
from .models import Contact

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



# Register your models here.

admin.site.register(Contact,ContactAdmin)
