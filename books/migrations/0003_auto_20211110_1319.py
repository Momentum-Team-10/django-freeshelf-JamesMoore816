# Generated by Django 3.2.9 on 2021-11-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='books.Category'),
        ),
    ]
