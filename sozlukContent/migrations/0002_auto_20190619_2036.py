# Generated by Django 2.2.2 on 2019-06-19 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sozlukContent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sozlukcontent',
            name='ekleyenId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
