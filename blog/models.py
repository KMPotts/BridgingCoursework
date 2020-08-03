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
        ('Working Knowledge', "Working Knowledge"),
        ('Proficient', "Proficient"),
        ('Fluent', "Fluent")
    ]

    skill = models.CharField(max_length = 200)
    proficiency = models.CharField(max_length = 17, choices=PROFICIENCY_OPTIONS, default = 'MID')

    def publish(self):
        self.save()

    def __str__(self):
        return self.skill

class AcademicObject(models.Model):
    institution = models.CharField(max_length = 200)
    details = models.TextField()
    gradYear = models.IntegerField(default = 2020)

    def publish(self):
        self.save()

    def __str__(self):
        return self.institution

class AchievementModel(models.Model):
    MONTH_OPTIONS = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    ]

    label = models.CharField(max_length = 200)
    year = models.IntegerField()
    month = models.CharField(max_length = 9, choices=MONTH_OPTIONS, default = 'January')
    details = models.TextField(null = True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.label

class InterestModel(models.Model):
    title = models.CharField(max_length = 200)
    details = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
