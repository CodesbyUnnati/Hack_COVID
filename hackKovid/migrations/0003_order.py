# Generated by Django 3.1.1 on 2020-09-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackKovid', '0002_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='', max_length=50)),
                ('itemsJson', models.CharField(default='', max_length=5000)),
                ('phone', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
