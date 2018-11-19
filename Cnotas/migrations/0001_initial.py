# Generated by Django 2.1.3 on 2018-11-19 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('semestre', models.CharField(max_length=60)),
                ('seccion', models.CharField(max_length=60)),
                ('jornada', models.CharField(max_length=60)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('docente', models.CharField(max_length=30)),
                ('creditos', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(through='Cnotas.Asignacion', to='Cnotas.Materia'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cnotas.Grado'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cnotas.Materia'),
        ),
    ]
