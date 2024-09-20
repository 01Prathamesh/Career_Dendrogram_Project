# Generated by Django 5.0.8 on 2024-09-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0007_testquestion_usertestresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testquestion',
            old_name='question_text',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='correct_option',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='testquestion',
            name='option4',
        ),
        migrations.AddField(
            model_name='testquestion',
            name='choices',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]