# Generated by Django 4.1.3 on 2022-12-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_alter_auction_auction_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='bider_user',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
