# Generated by Django 4.2.4 on 2023-08-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.ManyToManyField(to='MainApp.color'),
        ),
    ]
