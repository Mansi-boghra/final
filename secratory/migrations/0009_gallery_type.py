# Generated by Django 4.0 on 2022-03-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secratory', '0008_maintenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='type',
            field=models.CharField(choices=[('garden', 'garden'), ('gym', 'gym'), ('events', 'events'), ('society', 'society')], default='events', max_length=20),
        ),
    ]
