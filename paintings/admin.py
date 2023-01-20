from django.contrib import admin
from .models import Language, Genre, Painting, Artist, PaintingInstance

admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Painting)
admin.site.register(Artist)
admin.site.register(PaintingInstance)
