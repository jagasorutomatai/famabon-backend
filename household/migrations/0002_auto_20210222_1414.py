# Generated by Django 3.1.6 on 2021-02-22 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='household.tag'),
        ),
    ]
