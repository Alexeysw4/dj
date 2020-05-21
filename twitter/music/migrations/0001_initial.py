# Generated by Django 3.0.5 on 2020-05-20 18:01

import common.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Album title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/albums')),
                ('published', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'ordering': ['-published', 'author', 'title'],
                'get_latest_by': 'published',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Genre name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Genres',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/singers')),
            ],
            options={
                'verbose_name_plural': 'Singers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/songs')),
                ('track', models.FileField(upload_to='songs/%Y/%m/%d', validators=[common.validators.validate_file_extension])),
                ('published', models.DateField(blank=True, null=True)),
                ('clip_link', models.URLField(blank=True, null=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', related_query_name='songs', to='music.Album')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', related_query_name='songs', to='music.Genre')),
                ('singers', models.ManyToManyField(related_name='songs', to='music.Singer')),
            ],
            options={
                'verbose_name_plural': 'Songs',
                'ordering': ['-published', 'title'],
                'get_latest_by': 'published',
            },
        ),
        migrations.CreateModel(
            name='TrackUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners_set', related_query_name='owners_set', to='music.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks_set', related_query_name='tracks_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('added',),
            },
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', related_query_name='album', to='music.Singer'),
        ),
    ]