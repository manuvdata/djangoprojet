from django.db import models





class Anniversaire(models.Model):

    pdf = models.FileField(upload_to='', )



    def __str__(self):
        return self.title


