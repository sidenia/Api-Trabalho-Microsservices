from django.db import models

class Filmes(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'Filmes'
