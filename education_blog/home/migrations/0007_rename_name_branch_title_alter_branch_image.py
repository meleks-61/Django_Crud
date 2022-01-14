# Generated by Django 4.0.1 on 2022-01-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_branch_branch_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='branch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='branch'),
        ),
    ]