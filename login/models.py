# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class BranchCode(models.Model):
    branch_code_id = models.AutoField(primary_key=True)
    course_code = models.IntegerField()
    aicte_approved_status = models.CharField(max_length=3)
    branch_name = models.CharField(max_length=50)
    branch_code = models.IntegerField()
    department_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'branch_code'
        unique_together = (('branch_code_id', 'branch_code'),)
    
    def __str__(self):
        return self.branch_name


class CourseCode(models.Model):
    course_code_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_code'
        unique_together = (('course_code_id', 'course_code'),)

    def __str__(self):
        return self.course_name

