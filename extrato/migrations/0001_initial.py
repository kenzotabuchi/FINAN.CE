# Generated by Django 5.1.7 on 2025-03-29 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.categoria')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.conta')),
            ],
        ),
    ]
