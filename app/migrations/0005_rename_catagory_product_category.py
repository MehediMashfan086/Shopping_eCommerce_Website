# Generated by Django 3.2.7 on 2021-11-12 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
    ]