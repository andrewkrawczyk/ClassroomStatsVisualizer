# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
#user Profile set up Begin
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    
    def __str__(self):
        return f'{self.user.username} Profile'
        


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = [['group', 'permission']]


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = [['content_type', 'codename']]


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = [['user', 'group']]


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = [['user', 'permission']]


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = [['app_label', 'model']]


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Teacher(models.Model):
    teacher_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=4)
    first_name = models.TextField(max_length=25)
    last_name = models.TextField(max_length=25)

    class Meta:
        managed = False
        db_table = 'teacher'

  


class Student(models.Model):
    student_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=8)
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)
    first_name = models.TextField(max_length=25)
    last_name = models.TextField(max_length=25)
    truancy = models.DecimalField(decimal_places=0, max_digits=3)
    composite_score = models.DecimalField(decimal_places=0, max_digits=3)

    class Meta:
        managed = False
        db_table = 'student'


class Dra(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    entertime = models.DateTimeField()
    score = models.DecimalField(decimal_places=0, max_digits=3)

    class Meta:
        managed = False
        db_table = 'dra'
        unique_together = ('student', 'entertime')


class Ireadymath(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    entertime = models.DateTimeField()
    score = models.DecimalField(decimal_places=0, max_digits=3)

    class Meta:
        managed = False
        db_table = 'ireadymath'
        unique_together = ('student', 'entertime')


class Ireadyreading(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    entertime = models.DateTimeField()
    score = models.DecimalField(decimal_places=0, max_digits=3)

    class Meta:
        managed = False
        db_table = 'ireadyreading'
        unique_together = ('student', 'entertime')
