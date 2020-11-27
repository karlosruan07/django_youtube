from django.contrib import admin

from .models import Post #Aqui é chamado a classe do modelo que foi criado

admin.site.register(Post) #Aqui é registrado o modelo

# Register your models here.
