# Generated by Django 3.2.6 on 2021-12-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('user_mail_id', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
