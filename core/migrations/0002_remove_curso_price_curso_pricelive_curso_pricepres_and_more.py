# Generated by Django 4.2 on 2023-08-23 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='price',
        ),
        migrations.AddField(
            model_name='curso',
            name='pricelive',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Preço do Curso Online Ao Vivo'),
        ),
        migrations.AddField(
            model_name='curso',
            name='pricepres',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Preço do Curso Presencial'),
        ),
        migrations.AddField(
            model_name='curso',
            name='pricerec',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Preço do Curso Gravado'),
        ),
    ]
