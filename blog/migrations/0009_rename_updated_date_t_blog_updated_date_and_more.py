# Generated by Django 4.0.3 on 2022-03-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_created_date_t_blog_updated_date_t'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='updated_date_t',
            new_name='updated_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='created_date_t',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]