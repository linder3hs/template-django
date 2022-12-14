# Generated by Django 4.1.3 on 2022-12-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_teacherproxy_alter_studentproxy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('average_rating', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('isbn13', models.CharField(max_length=200)),
                ('language_code', models.CharField(max_length=200)),
                ('num_pages', models.CharField(max_length=200)),
                ('ratings_count', models.IntegerField(default=0)),
                ('text_reviews_count', models.IntegerField(default=0)),
                ('publication_date', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='studentproxy',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
