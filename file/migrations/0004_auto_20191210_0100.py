# Generated by Django 2.2.2 on 2019-12-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20191210_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='documento_ventas',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='entrega',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='ident_fiscal',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='material',
            field=models.CharField(max_length=30),
        ),
    ]
