# Generated by Django 4.0.3 on 2022-06-11 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaUsuario',
            fields=[
                ('idCategoriaUsusario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreCategriaUsuario', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='imagenProducto',
            field=models.FileField(default='https://www.cotopaxi.com.ec/sites/default/files/2020-08/BLANCO%20760X440PX_0.png', upload_to=''),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
                ('rutUsuario', models.CharField(max_length=10, unique=True)),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('direccionUsusario', models.CharField(max_length=100)),
                ('suscripcionUsusario', models.BooleanField()),
                ('contraseñaUsuario', models.CharField(max_length=50)),
                ('imagenUsuario', models.FileField(upload_to='')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoriausuario')),
            ],
        ),
    ]