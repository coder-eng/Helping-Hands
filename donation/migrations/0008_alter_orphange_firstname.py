# Generated by Django 4.0.4 on 2022-05-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0007_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orphange',
            name='firstName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]