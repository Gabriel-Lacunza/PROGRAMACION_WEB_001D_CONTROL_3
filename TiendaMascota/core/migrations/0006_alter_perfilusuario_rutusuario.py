# Generated by Django 4.0.5 on 2022-07-01 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_perfilusuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='rutUsuario',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
