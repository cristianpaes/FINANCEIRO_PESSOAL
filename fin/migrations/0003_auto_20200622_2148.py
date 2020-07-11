# Generated by Django 3.0.7 on 2020-06-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0002_auto_20200619_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salario',
            name='data_extra',
            field=models.DateField(verbose_name='Data do Extra'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='data_sal',
            field=models.DateField(verbose_name='Data do Salário'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='valor_extra',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor do Extra'),
        ),
    ]
