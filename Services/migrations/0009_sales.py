# Generated by Django 3.1.7 on 2021-05-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0008_civildata_electricaldata_itdata_mechanicaldata_sciencedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('price', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
