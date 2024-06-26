# Generated by Django 5.0.3 on 2024-03-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGed', '0002_alter_document_remarque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='extention',
            field=models.CharField(choices=[('pdf', 'Fichier Pdf'), ('docx', 'Document Word'), ('xlsx', 'Tableau Excel'), ('txt', 'Fichier Plat')], default='pdf', max_length=5),
        ),
        migrations.AlterField(
            model_name='document',
            name='remarque',
            field=models.TextField(max_length=512),
        ),
    ]
