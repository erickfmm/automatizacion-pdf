# Generated by Django 4.1.6 on 2023-02-10 15:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=64)),
                ('rut', models.CharField(max_length=18)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='comentario',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='report',
            name='decision',
            field=models.CharField(default='revisar', max_length=32),
        ),
        migrations.AddField(
            model_name='report',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='report',
            name='id_persona',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mainapp.persona'),
        ),
    ]