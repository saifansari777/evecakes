# Generated by Django 3.0.4 on 2020-04-01 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Cakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('weight', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('weight_unit', models.CharField(choices=[('KG', 'kilogram'), ('G', 'Grams')], max_length=40)),
                ('vegetrian', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('discounted', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/placeholder.png', upload_to='images/')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('flavour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Flavour')),
            ],
        ),
    ]
