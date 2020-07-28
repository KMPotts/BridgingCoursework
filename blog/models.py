from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CodingSkill(models.Model):
    PROFICIENCY_OPTIONS = [
        ('LOW', "Working Knowledge"),
        ('MID', "Proficient"),
        ('HIGH', "Fluent")
    ]

    skill = models.CharField(max_length = 200)
    proficiency = models.CharField(max_length = 4, choices=PROFICIENCY_OPTIONS, default = 'MID')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class AcademicObject(models.Model):
    institution = models.CharField(max_length = 200)
    details = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class AchievementModel(models.Model):
    MONTH_OPTIONS = [
        ('JAN', 'January'),
        ('FEB', 'February'),
        ('MAR', 'March'),
        ('APR', 'April'),
        ('MAY', 'May'),
        ('JUN', 'June'),
        ('JUL', 'July'),
        ('AUG', 'August'),
        ('SEP', 'September'),
        ('OCT', 'October'),
        ('NOV', 'November'),
        ('DEC', 'December')
    ]

    label = models.CharField(max_length = 200)
    year = models.IntegerField()
    month = models.CharField(max_length = 3, choices=MONTH_OPTIONS, default = 'JAN')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class InterestModel(models.Model):
    title = models.CharField(max_length = 200)
    details = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
