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


class StudentInfo(models.Model):
    student_info_id = models.AutoField(primary_key=True)
    course_code = models.ForeignKey(CourseCode, on_delete=models.CASCADE, db_column='course_code')
    branch_code = models.ForeignKey(BranchCode, on_delete=models.CASCADE, db_column='branch_code')
    shift = models.CharField(max_length=6, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    admission_year = models.IntegerField(blank=True, null=True)
    sc_st_category = models.CharField(max_length=20, blank=True, null=True)
    gill_quota = models.CharField(max_length=1, blank=True, null=True)
    hostel_facility = models.CharField(max_length=20, blank=True, null=True)
    college_roll_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    university_roll_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ssection = models.CharField(max_length=20)
    sgroup = models.CharField(max_length=20)
    leet_non_leet = models.CharField(max_length=8, blank=True, null=True)
    fws = models.CharField(max_length=1, blank=True, null=True)
    sfname = models.CharField(max_length=50, blank=True, null=True)
    smname = models.CharField(max_length=50, blank=True, null=True)
    ssname = models.CharField(max_length=50, blank=True, null=True)
    ffname = models.CharField(max_length=50, blank=True, null=True)
    fmname = models.CharField(max_length=50, blank=True, null=True)
    fsname = models.CharField(max_length=50, blank=True, null=True)
    mfname = models.CharField(max_length=50, blank=True, null=True)
    mmname = models.CharField(max_length=50, blank=True, null=True)
    msname = models.CharField(max_length=12, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    blood_group = models.CharField(max_length=9, blank=True, null=True)
    martial_status = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length=6, blank=True, null=True)
    c_address_type = models.CharField(max_length=7, blank=True, null=True)
    c_address_line_1 = models.CharField(max_length=500, blank=True, null=True)
    c_address_line_2 = models.CharField(max_length=500, blank=True, null=True)
    c_city_name = models.CharField(max_length=39, blank=True, null=True)
    c_vpo = models.CharField(max_length=52, blank=True, null=True)
    c_pincode = models.CharField(max_length=7, blank=True, null=True)
    c_tehsil = models.CharField(max_length=19, blank=True, null=True)
    c_district = models.CharField(max_length=37, blank=True, null=True)
    c_state = models.CharField(max_length=17, blank=True, null=True)
    p_address_type = models.CharField(max_length=7, blank=True, null=True)
    p_address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    p_address_line_2 = models.CharField(max_length=66, blank=True, null=True)
    p_city_name = models.CharField(max_length=25, blank=True, null=True)
    p_vpo = models.CharField(max_length=52, blank=True, null=True)
    p_pincode = models.CharField(max_length=14, blank=True, null=True)
    p_tehsil = models.CharField(max_length=19, blank=True, null=True)
    p_district = models.CharField(max_length=37, blank=True, null=True)
    p_state = models.CharField(max_length=17, blank=True, null=True)
    father_mobile_no = models.BigIntegerField(blank=True, null=True)
    mother_mobile_no = models.CharField(max_length=24, blank=True, null=True)
    residence_phone_no = models.CharField(max_length=13, blank=True, null=True)
    residence_phone_no_std = models.CharField(max_length=12, blank=True, null=True)
    parents_annual_income = models.CharField(max_length=23, blank=True, null=True)
    student_mobile_no = models.CharField(max_length=11, blank=True, null=True)
    father_email = models.CharField(max_length=50, blank=True, null=True)
    mother_email = models.CharField(max_length=50, blank=True, null=True)
    student_email = models.CharField(max_length=50, blank=True, null=True)
    father_qualification = models.CharField(max_length=56, blank=True, null=True)
    father_occupation = models.CharField(max_length=50, blank=True, null=True)
    father_office_address = models.CharField(max_length=500, blank=True, null=True)
    father_office_phone = models.CharField(max_length=18, blank=True, null=True)
    father_office_phone_std = models.CharField(max_length=14, blank=True, null=True)
    mother_qualification = models.CharField(max_length=38, blank=True, null=True)
    mother_occupation = models.CharField(max_length=50, blank=True, null=True)
    mother_office_address = models.CharField(max_length=500, blank=True, null=True)
    mother_office_phone = models.CharField(max_length=19, blank=True, null=True)
    mother_office_phone_std = models.CharField(max_length=14, blank=True, null=True)
    student_status = models.CharField(max_length=6)
    religion = models.CharField(max_length=9, blank=True, null=True)
    student_category = models.CharField(max_length=20, blank=True, null=True)
    aicte_rc = models.CharField(max_length=10)
    full_part_time = models.CharField(max_length=10)
    remarks = models.TextField()
    fee_paid_status = models.CharField(max_length=1)
    eligibility = models.CharField(max_length=1)
    batch = models.IntegerField()
    advisor_id = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'student_info'

    def __str__(self):
        return self.university_roll_no

class SgpaInfo(models.Model):
    university_roll_no  = models.AutoField(primary_key=True)
    sem_1               = models.FloatField(blank=True, null=True, default=None)
    credits_1           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_1   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_1  = models.FloatField(blank=True, null=True, default=None)
    sem_2               = models.FloatField(blank=True, null=True, default=None)
    credits_2           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_2   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_2  = models.FloatField(blank=True, null=True, default=None)
    sem_3               = models.FloatField(blank=True, null=True, default=None)
    credits_3           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_3   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_3  = models.FloatField(blank=True, null=True, default=None)
    sem_4               = models.FloatField(blank=True, null=True, default=None)
    credits_4           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_4   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_4  = models.FloatField(blank=True, null=True, default=None)
    sem_5               = models.FloatField(blank=True, null=True, default=None)
    credits_5           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_5   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_5  = models.FloatField(blank=True, null=True, default=None)
    sem_6               = models.FloatField(blank=True, null=True, default=None)
    credits_6           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_6   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_6  = models.FloatField(blank=True, null=True, default=None)
    sem_7               = models.FloatField(blank=True, null=True, default=None)
    credits_7           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_7   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_7  = models.FloatField(blank=True, null=True, default=None)
    sem_8               = models.FloatField(blank=True, null=True, default=None)
    credits_8           = models.FloatField(blank=True, null=True, default=None)
    active_backlogs_8   = models.FloatField(blank=True, null=True, default=None)
    passive_backlogs_8  = models.FloatField(blank=True, null=True, default=None)
    
    @property
    def aggregate_sgpa(self):
        return (self.sem_1+self.sem_2+self.sem_3+self.sem_4+self.sem_5+self.sem_6+self.sem_7+self.sem_8)/2
    
    class Meta:
        db_table = 'sgpa_info'