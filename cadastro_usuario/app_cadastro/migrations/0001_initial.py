# Generated by Django 5.0.3 on 2024-03-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    iniuser_imgl = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('renda_mensal', models.DecimalField(decimal_places=2, max_digits=15)),
                ('credito', models.FloatField(default=0.0)),
            ],
        ),
    ]
