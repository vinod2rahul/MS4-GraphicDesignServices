# Generated by Django 3.2.5 on 2021-07-22 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphicdesignapp', '0007_design_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='desciption',
            new_name='description',
        ),
    ]