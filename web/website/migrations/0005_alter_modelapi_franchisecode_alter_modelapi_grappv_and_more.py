# Generated by Django 4.2.11 on 2024-03-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_modelapi_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelapi',
            name='FranchiseCode',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='GrAppv',
            field=models.IntegerField(default=280000),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='LowDoc',
            field=models.CharField(default='Y', max_length=3),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='NAICS_digit',
            field=models.IntegerField(default=62),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='RevLineCr',
            field=models.CharField(default='N', max_length=3),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='SBA_Appv',
            field=models.IntegerField(default=210000),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='Term',
            field=models.FloatField(default=180),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='UrbanRural',
            field=models.FloatField(default=0),
        ),
    ]