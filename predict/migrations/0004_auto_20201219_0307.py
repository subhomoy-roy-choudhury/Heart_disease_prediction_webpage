# Generated by Django 3.1.4 on 2020-12-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_auto_20201218_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults2',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='ca',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='chol',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='cp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='exang',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='fbs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='oldpeak',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='restecg',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='sex',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='slope',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='target',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='thal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='thalach',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults2',
            name='trestbps',
            field=models.IntegerField(),
        ),
    ]