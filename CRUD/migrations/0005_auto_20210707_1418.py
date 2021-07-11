# Generated by Django 3.2 on 2021-07-07 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CRUD', '0004_rename_name_customerdetails_assignto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
