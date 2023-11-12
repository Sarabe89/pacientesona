# Generated by Django 4.2.3 on 2023-11-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes_2023', '0007_paciente_anotaciones_paciente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='servicio',
            field=models.CharField(blank=True, choices=[('Clinica Medica', 'Clinica Medica'), ('Guardia Adultos', 'Guardia de Adultos'), ('Maternidad', 'Maternidad'), ('Neo', 'Neo'), ('Partos', 'Partos'), ('Pediatria Guardia', 'Pedriatria Guardia'), ('Pediatria Internacion', 'Pediatria Internacion'), ('Polivalente', 'Polivalente'), ('Quirofano', 'Quirofano'), ('UCI', 'UCI'), ('UTI', 'UTI'), ('Coordinacion', 'Coordinacion'), ('Casa de Madres', 'Casa de Madres')], max_length=50, null=True),
        ),
    ]