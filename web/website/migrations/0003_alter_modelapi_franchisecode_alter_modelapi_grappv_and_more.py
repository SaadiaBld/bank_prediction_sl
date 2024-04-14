# Generated by Django 4.2.11 on 2024-03-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_modelapi_naics_remove_modelapi_newexist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelapi',
            name='FranchiseCode',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='GrAppv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='LowDoc',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='NAICS_digit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='RevLineCr',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='SBA_Appv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='Term',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='UrbanRural',
            field=models.FloatField(),
        ),
    ]