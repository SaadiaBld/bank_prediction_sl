# Generated by Django 4.2.11 on 2024-03-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelapi',
            name='NAICS',
        ),
        migrations.RemoveField(
            model_name='modelapi',
            name='NewExist',
        ),
        migrations.RemoveField(
            model_name='user',
            name='website_groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='website_user_permissions',
        ),
        migrations.AddField(
            model_name='modelapi',
            name='FranchiseCode',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='modelapi',
            name='GrAppv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modelapi',
            name='NAICS_digit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modelapi',
            name='SBA_Appv',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='Term',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='modelapi',
            name='UrbanRural',
            field=models.FloatField(default=0),
        ),
    ]
