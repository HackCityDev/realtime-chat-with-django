# Generated by Django 4.2.6 on 2023-10-26 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_customuser_id"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Post",
            new_name="BlogPost",
        ),
    ]