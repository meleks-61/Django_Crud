# Generated by Django 4.0 on 2022-01-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog3', '0012_alter_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='Name', max_length=100, verbose_name='Name'),
        ),
    ]
