from django.db import models
from simple_history.models import HistoricalRecords

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя", null=True)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", null=True)
    university = models.CharField(max_length=200, verbose_name="Название ВУЗа", null=True)
    faculty = models.CharField(max_length=200, verbose_name="Название факультета", null=True)
    course_number = models.PositiveIntegerField(verbose_name="Номер курса", null=True)

    history = HistoricalRecords()  

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.university})"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название проекта", null=True)
    field = models.CharField(max_length=200, verbose_name="Направление проекта", null=True)
    students = models.ManyToManyField(Student, related_name="projects", verbose_name="Участники")
    description = models.TextField(blank=True, verbose_name="Описание проекта", null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название мероприятия", null=True)
    field = models.CharField(max_length=200, verbose_name="Направление проекта", null=True)
    students = models.ManyToManyField(Student, related_name="events", verbose_name="Участники")
    description = models.TextField(blank=True, verbose_name="Описание мероприятия", null=True)
    address = models.CharField(max_length=300, verbose_name="Адрес проведения", null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.title
