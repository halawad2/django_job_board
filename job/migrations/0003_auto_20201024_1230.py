# Generated by Django 2.2.7 on 2020-10-24 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_remove_category_cat_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.Category'),
        ),
    ]