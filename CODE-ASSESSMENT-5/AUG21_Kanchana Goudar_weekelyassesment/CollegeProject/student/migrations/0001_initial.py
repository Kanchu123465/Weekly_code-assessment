# Generated by Django 3.2.6 on 2021-08-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Admo', models.IntegerField()),
                ('Rollno', models.IntegerField()),
                ('College', models.CharField(max_length=50)),
                ('Parentname', models.CharField(max_length=50)),
            ],
        ),
    ]
