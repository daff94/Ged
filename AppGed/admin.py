from django.contrib import admin
from .models import User, Document, Categorie, Groupe


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email','password')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('nom_document','remarque','piecejointe','groupe','categorie')
    search_fields = ['nom_document','remarque']
    list_per_page = 10
    

admin.site.register(Categorie)
admin.site.register(Groupe)