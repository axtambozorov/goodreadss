# Generated by Django 3.1.14 on 2022-03-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20220328_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_picture',
            field=models.ImageField(default='book.jpg', upload_to=''),
        ),
    ]
