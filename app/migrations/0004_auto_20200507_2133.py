# Generated by Django 2.1.7 on 2020-05-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='/static/assets/img/image-placeholder.jpg', upload_to='static/assets/img/'),
        ),
    ]
