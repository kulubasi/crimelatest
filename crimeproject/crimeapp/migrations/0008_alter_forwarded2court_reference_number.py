# Generated by Django 4.1.2 on 2022-11-04 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0007_alter_forwarded2court_crimescene_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forwarded2court',
            name='Reference_Number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
