# Generated by Django 4.2.3 on 2023-11-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes_2023', '0008_alter_paciente_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cama',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='habitacion',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
