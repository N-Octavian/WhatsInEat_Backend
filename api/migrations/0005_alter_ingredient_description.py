# Generated by Django 4.0.2 on 2022-03-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_ingredient_description_alter_ingredient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='description',
            field=models.TextField(),
        ),
    ]
