# Generated by Django 4.2.4 on 2023-08-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_journal_content_alter_journal_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='urlToImage',
            field=models.ImageField(upload_to=' Images'),
        ),
    ]
