# Generated by Django 3.0.3 on 2020-02-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]
