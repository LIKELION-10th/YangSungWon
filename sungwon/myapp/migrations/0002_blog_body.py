# Generated by Django 4.0.5 on 2022-07-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
