# Generated by Django 2.2.17 on 2021-01-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflow', '0010_auto_20210107_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(related_name='tags', to='stackoverflow.Question'),
        ),
    ]