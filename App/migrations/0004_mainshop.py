# Generated by Django 3.0.3 on 2020-08-12 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_mainmustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.CharField(default=1, max_length=1000000)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
