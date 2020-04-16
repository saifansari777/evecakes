# Generated by Django 3.0.5 on 2020-04-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('core', '0005_auto_20200414_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=140)),
            ],
        ),
        migrations.RenameModel(
            old_name='Cake',
            new_name='Item',
        ),
        migrations.RenameField(
            model_name='dealoftheday',
            old_name='cake',
            new_name='item',
        ),
    ]
