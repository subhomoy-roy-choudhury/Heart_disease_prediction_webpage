# Generated by Django 3.1.4 on 2020-12-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_predresults2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults2',
            name='age',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='chol',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='thalach',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='trestbps',
            field=models.FloatField(),
        ),
    ]
