# Generated by Django 2.2.2 on 2019-11-21 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='foto',
        ),
        migrations.AddField(
            model_name='perfil',
            name='cargo',
            field=models.CharField(max_length=10, null='false'),
            preserve_default='false',
        ),
    ]
