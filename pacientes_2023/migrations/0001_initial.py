# Generated by Django 4.2.1 on 2023-07-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('habitacion', models.CharField(max_length=80)),
                ('cama', models.CharField(max_length=80)),
                ('servicio', models.CharField(choices=[('Polivalente', 'Polivalente'), ('Clinica Medica', 'Clinica Medica'), ('Guardia Adultos', 'Guarda de Adultos'), ('Neo', 'Neo'), ('UTI', 'UTI'), ('UCI', 'UCI'), ('Pedriatria Guardia', 'Pedriatria Guardia'), ('Pediatria Internacion', 'Pediatria Internacion')], max_length=50)),
            ],
        ),
    ]
