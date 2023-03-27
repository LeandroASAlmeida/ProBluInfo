# Generated by Django 4.0.4 on 2023-01-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='carga_horaria',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='vl_curso',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salas',
            name='capacidade',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=6),
        ),
    ]