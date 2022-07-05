# Generated by Django 4.0.5 on 2022-06-24 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoría')),
                ('nombreCategoria', models.CharField(max_length=80, verbose_name='Nombre de la categoría')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaUsuario',
            fields=[
                ('idCategoriaUsusario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Categoria Usuario')),
                ('nombreCategriaUsuario', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutUsuario', models.CharField(max_length=10, unique=True)),
                ('nombreUsuario', models.CharField(max_length=100, verbose_name='Nombre Usuario')),
                ('apellidoUsuario', models.CharField(max_length=100, verbose_name='Apellido Usuario')),
                ('direccionUsusario', models.CharField(max_length=300, verbose_name='Direccion Usuario')),
                ('suscripcionUsusario', models.BooleanField(default=False, verbose_name='Suscriptor')),
                ('contraseñaUsuario', models.CharField(max_length=50, verbose_name='Contraseña')),
                ('imagenUsuario', models.ImageField(default='sinfoto.jpg', upload_to='images/', verbose_name='Imagen Usuario')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.categoriausuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('nomProducto', models.CharField(max_length=80, verbose_name='Nombre Producto')),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('porcDesctoSubscriptor', models.IntegerField(default=0, verbose_name='Porcentaje Descuento Suscriptor')),
                ('porcDesctoOferta', models.IntegerField(default=0, verbose_name='Porcentaje Descuento Oferta')),
                ('imagen', models.ImageField(default='sinfoto.jpg', upload_to='images/', verbose_name='Imagen Producto')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.categoria')),
            ],
        ),
    ]
