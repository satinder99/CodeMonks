from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin

@admin.register(BranchCode)
@admin.register(CourseCode)
@admin.register(StudentInfo)
@admin.register(SgpaInfo)

class CourseCodeAdmin(VersionAdmin):

    pass
class StudentInfoAdmin(VersionAdmin):

    pass
class SgpaInfoAdmin(VersionAdmin):

    pass
class BranchCodeAdmin(VersionAdmin):

    pass

'''
# Register your models here.
admin.site.register(BranchCode)
admin.site.register(CourseCode)
admin.site.register(StudentInfo)
admin.site.register(SgpaInfo)
'''
