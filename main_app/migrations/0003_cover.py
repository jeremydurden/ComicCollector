# Generated by Django 3.1.2 on 2020-12-14 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201210_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.comic')),
            ],
        ),
    ]