# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
        unique_together = [['student', 'entertime']]


class Ireadymath(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    entertime = models.DateTimeField()
    score = models.DecimalField(decimal_places=0, max_digits=3)

    class Meta:
        managed = False
        db_table = 'ireadymath'
        unique_together = [['student', 'entertime']]


class Ireadyreading(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    entertime = models.DateTimeField()
    score = models.DecimalField(decimal_places=0, max_digits=3)

    class Meta:
        managed = False
        db_table = 'ireadyreading'
        unique_together = [['student', 'entertime']]
