from django.contrib import admin
from groups import models 

# Register your models here.

# does not require registering
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)