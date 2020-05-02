from django.db import models


class Summaries(models.Model):

    id = models.AutoField(primary_key=True)
    summary = models.TextField(default=None)

    class Meta:

        # database table name
        db_table = 'summaries'
