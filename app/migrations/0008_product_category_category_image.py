# Generated by Django 2.1.7 on 2020-06-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200609_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='category_image',
            field=models.ImageField(blank=True, default='/static/assets/img/image-placeholder.jpg', max_length=255, null=True, upload_to=''),
        ),
    ]
