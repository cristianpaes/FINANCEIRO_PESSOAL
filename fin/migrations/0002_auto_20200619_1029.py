# Generated by Django 3.0.7 on 2020-06-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salario',
            name='data_reg_sal',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='data_dep',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='salario',
            name='data_extra',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='salario',
            name='data_sal',
            field=models.DateField(),
        ),
    ]
