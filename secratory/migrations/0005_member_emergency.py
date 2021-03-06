# Generated by Django 4.0 on 2022-02-07 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secratory', '0004_alter_adminsec_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('pic', models.FileField(default='avtar.jpg', upload_to='member')),
                ('flat_no', models.IntegerField()),
                ('wing', models.CharField(max_length=2)),
                ('address', models.TextField(blank=True, null=True)),
                ('doc_type', models.CharField(max_length=20)),
                ('doc_num', models.CharField(max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('role', models.BooleanField(default=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secratory.adminsec')),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('occup', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secratory.adminsec')),
            ],
        ),
    ]
