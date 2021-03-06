# Generated by Django 3.2 on 2022-01-15 21:20

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0005_auto_20220115_1940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='table',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='table',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(max_length=200, unique='True'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(default='', max_length=100, unique='True'),
        ),
        migrations.AlterField(
            model_name='table',
            name='reserve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
