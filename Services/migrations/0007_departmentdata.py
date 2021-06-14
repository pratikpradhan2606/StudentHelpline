# Generated by Django 3.1.7 on 2021-05-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('fname', models.CharField(default='', max_length=200)),
                ('lname', models.CharField(default='', max_length=200)),
                ('mobileno', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('desc', models.CharField(default='...', max_length=200)),
            ],
        ),
    ]
