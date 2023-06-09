# Generated by Django 4.1.7 on 2023-03-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.TextField(max_length=30)),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('pw', models.TextField()),
                ('phonenum', models.CharField(max_length=30)),
                ('schoolssn', models.TextField(null=True)),
            ],
        ),
    ]
