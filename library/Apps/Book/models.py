from django.db import models


class Autor(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200, blank = False, null = False)
    lastname = models.CharField(max_length = 200, blank = False, null = False)
    nationality = models.CharField(max_length = 200, blank = False, null = False)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return "" + self.name + " " + self.lastname

    class Meta:
        db_table = 'Authors'
        managed = True
        verbose_name = 'Autor'
        verbose_name_plural = 'Authors'
