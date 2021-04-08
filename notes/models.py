from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length = 200, null = True)

class Note(models.Model):
    title = models.CharField(max_length=200, null = True)
    content = models.TextField(null = True)
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return str(self.id) + ". " + self.title
