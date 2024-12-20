# Generated by Django 5.0.8 on 2024-12-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]