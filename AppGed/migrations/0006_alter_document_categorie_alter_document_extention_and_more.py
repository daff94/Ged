# Generated by Django 5.0.3 on 2024-03-24 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGed', '0005_remove_document_chemin_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AppGed.categorie', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='document',
            name='extention',
            field=models.CharField(choices=[('pdf', 'Fichier Pdf'), ('docx', 'Document Word'), ('xlsx', 'Tableau Excel'), ('txt', 'Fichier Plat'), ('html', 'Lien Internet')], default='pdf', max_length=5, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='document',
            name='nom_document',
            field=models.CharField(max_length=50, verbose_name='Nom du Document'),
        ),
    ]
