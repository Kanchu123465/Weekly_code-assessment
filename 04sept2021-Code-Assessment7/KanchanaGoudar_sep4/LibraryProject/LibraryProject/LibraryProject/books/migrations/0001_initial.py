# Generated by Django 3.2.7 on 2021-09-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=50)),
                ('Des', models.CharField(max_length=50)),
                ('Price', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=50)),
            ],
        ),
    ]
