# Generated by Django 5.0.6 on 2024-07-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='institution_number',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='swift_code',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='transit_number',
        ),
        migrations.AlterField(
            model_name='bank',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
