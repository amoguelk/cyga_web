# Generated by Django 4.2.3 on 2024-05-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name_plural': 'Content'},
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('SL', 'Slide'), ('AM', 'Additional material')], default='AM', max_length=30),
        ),
    ]