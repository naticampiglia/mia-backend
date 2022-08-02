# Generated by Django 3.0 on 2020-09-06 22:49

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaSintoma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=255)),
                ('pregunta', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EntradaDiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=None, null=True)),
                ('coordenadas', django.contrib.gis.db.models.fields.PointField(default=None, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRespuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=255, unique=True)),
                ('opciones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='ValorRespuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(blank=True, max_length=25)),
                ('entrada_diario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='symptoms.EntradaDiario')),
                ('pregunta_diario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='symptoms.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Sintoma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='symptoms.CategoriaSintoma')),
            ],
            options={
                'verbose_name': 'Síntoma historial',
                'verbose_name_plural': 'Síntomas historiales',
            },
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tipo_respuesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='symptoms.TipoRespuesta'),
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sintomas', models.ManyToManyField(to='symptoms.Sintoma')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entradadiario',
            name='pregunta_diario',
            field=models.ManyToManyField(through='symptoms.ValorRespuesta', to='symptoms.Pregunta'),
        ),
        migrations.AddField(
            model_name='entradadiario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
