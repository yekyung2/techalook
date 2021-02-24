# Generated by Django 2.2.5 on 2021-02-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(default='')),
                ('title', models.TextField(default='')),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('directory', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Techblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
