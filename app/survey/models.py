from django.db import models

class SurveyForm(models.Model):
    PRIVACY= (
        ('public', 'Public'),
        ('private', 'Private'),
        ('password', 'Password'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    categories = models.CharField(max_length=255, blank=True)
    privacy = models.CharField(max_length=50,choices=PRIVACY)
    password = models.CharField(max_length=128, blank=True, null=True)
    data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
