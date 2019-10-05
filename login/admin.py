from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin



@admin.register(CourseCode)
class CourseCode(VersionAdmin):

    recover_form_template = 'reversion/recover_form.html'
@admin.register(StudentInfo)
class StudentInfo(VersionAdmin):
    recover_form_template = 'reversion/recover_form.html'

@admin.register(SgpaInfo)
class SgpaInfo(VersionAdmin):

    recover_form_template = 'reversion/recover_form.html'
@admin.register(BranchCode)
class BranchCode(VersionAdmin):

    recover_form_template = 'reversion/recover_form.html'

'''
# Register your models here.
admin.site.register(BranchCode)
admin.site.register(CourseCode)
admin.site.register(StudentInfo)
admin.site.register(SgpaInfo)
'''
