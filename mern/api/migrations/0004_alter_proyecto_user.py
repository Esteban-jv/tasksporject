# Generated by Django 3.2.9 on 2021-12-07 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20211207_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='user',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
        ),
    ]
