# Generated by Django 3.1.7 on 2021-03-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='item_details',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='item_name',
        ),
        migrations.AddField(
            model_name='post',
            name='item_type',
            field=models.CharField(choices=[('DRAFTERS', 'Drafters'), ('BOOKS', 'Books'), ('CYCLES', 'Cycles'), ('OTHER', 'Other (Mattress,Mirror,Laundry Baskets/Hangers,etc')], default='OTHER', max_length=10),
        ),
    ]
