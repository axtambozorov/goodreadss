# Generated by Django 3.1.14 on 2022-03-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='rasm.jpg', upload_to=''),
        ),
    ]