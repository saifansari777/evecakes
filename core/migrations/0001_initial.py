# Generated by Django 3.0.5 on 2020-04-13 12:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/%Y/%m/%d/placeholder.png', upload_to='images/%Y/%m/%d/')),
                ('image2', models.ImageField(default='images/%Y/%m/%d/placeholder.png', upload_to='images/%Y/%m/%d/')),
                ('image3', models.ImageField(blank=True, default='images/%Y/%m/%d/placeholder.png', null=True, upload_to='images/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('weight_unit', models.CharField(choices=[('KG', 'kilogram'), ('Gm', 'Grams')], max_length=40)),
                ('vegetrian', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('discounted', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/%Y/%m/%d/placeholder.png', upload_to='images/%Y/%m/%d/')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='DealOfTheDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discounted_price', models.PositiveIntegerField()),
                ('normal_price', models.PositiveIntegerField()),
                ('item_image', models.ImageField(blank=True, default='images/%Y/%m/%d/placeholder.png', null=True, upload_to='images/%Y/%m/%d/')),
                ('endtime', models.DateTimeField(default=datetime.datetime(2020, 4, 14, 6, 16, 5, 590908))),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cake')),
            ],
        ),
        migrations.AddField(
            model_name='cake',
            name='flavour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Flavour'),
        ),
    ]
