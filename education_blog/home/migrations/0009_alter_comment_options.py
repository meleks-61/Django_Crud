# Generated by Django 4.0.1 on 2022-01-14 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date', 'id']},
        ),
    ]