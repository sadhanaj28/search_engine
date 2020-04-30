from django.db import models


# Create your models here.
class Summaries(models.Model):

    id = models.AutoField(primary_key=True)
    summary = models.TextField(default=None)

    class Meta:
        db_table = 'summaries'
