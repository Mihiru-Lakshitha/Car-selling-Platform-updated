# Generated by Django 4.0.3 on 2023-12-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_auctionlisting_image_url_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='Guest.png', upload_to='avatars/'),
        ),
    ]
