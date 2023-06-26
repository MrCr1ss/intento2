# Generated by Django 4.1.1 on 2022-12-06 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appLibros', '0003_autor_fechanacimiento_alter_autor_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appLibros.autor', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(max_length=100, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='paginas',
            field=models.IntegerField(verbose_name='Páginas'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]