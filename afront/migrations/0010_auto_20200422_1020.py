# Generated by Django 3.0.5 on 2020-04-22 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afront', '0009_auto_20200422_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biorythmsmodel',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='afront.Human'),
        ),
    ]