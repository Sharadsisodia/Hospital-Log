# Generated by Django 5.0.7 on 2024-07-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formlogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='d_Pincode',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_Pincode',
            field=models.CharField(max_length=14),
        ),
    ]