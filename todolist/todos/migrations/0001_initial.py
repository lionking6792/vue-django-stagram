# Generated by Django 2.2.6 on 2019-10-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=350, verbose_name='body')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create_at')),
            ],
        ),
    ]
