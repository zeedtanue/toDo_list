# Generated by Django 2.0.5 on 2018-10-08 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=140, unique=True)),
            ],
        ),
    ]
