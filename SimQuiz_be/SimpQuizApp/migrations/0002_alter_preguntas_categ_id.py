# Generated by Django 3.2.7 on 2023-07-12 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SimpQuizApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='categ_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SimpQuizApp.categorias'),
        ),
    ]
