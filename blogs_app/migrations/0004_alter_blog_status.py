# Generated by Django 5.0.4 on 2024-05-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0003_rename_categroy_blog_category_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='Draft', max_length=20),
        ),
    ]
