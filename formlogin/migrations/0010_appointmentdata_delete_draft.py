# Generated by Django 5.0.7 on 2024-08-08 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formlogin', '0009_imagepost_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointmentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_username', models.CharField(max_length=20)),
                ('ap_specilist', models.CharField(max_length=30)),
                ('ap_date', models.DateField()),
                ('ap_startTime', models.TimeField()),
                ('ap_endTime', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='draft',
        ),
    ]
