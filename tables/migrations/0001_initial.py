# Generated by Django 3.2 on 2022-01-15 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persons', models.IntegerField()),
                ('twochairs', models.IntegerField()),
                ('fourchairs', models.IntegerField()),
                ('party', models.IntegerField()),
                ('free', models.BooleanField(default=True)),
                ('reserve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.guest')),
            ],
        ),
    ]
