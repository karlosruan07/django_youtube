from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Essa classe serve para criar um novo modelo, ela tem que ser chamado no arquivo admin
class Post(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    conteudo = models.TextField()

# Create your models here.
