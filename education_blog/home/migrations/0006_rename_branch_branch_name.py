# Generated by Django 4.0.1 on 2022-01-13 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_branch_image_branch_slug_teacher_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='branch',
            new_name='name',
        ),
    ]
