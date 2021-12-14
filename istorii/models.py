# models.py
from django.db import models

# Create your models here.

# choices for new action field in Action
'''
ACTION_CHOICES = (
    ('create', _('Create')),
    ('read', _('Read')),
    ('update', _('Update')),
    ('publish', _('Publish')),
)
'''

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)


class TextTag(models.Model):
    id = models.AutoField(primary_key=True)
    text_tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.text_tag


class Text(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    tag = models.ForeignKey(TextTag, on_delete=models.CASCADE)
    annotation = models.TextField()


class Action(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    text_id = models.ForeignKey(Text, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action

    class Meta:
        db_table = 'action'
        unique_together = (('person_id', 'text_id'),)
