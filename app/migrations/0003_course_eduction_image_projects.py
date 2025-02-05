# Generated by Django 4.0 on 2025-01-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_filefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='static/image')),
                ('title', models.CharField(default='title', max_length=255)),
                ('company', models.CharField(default='company', max_length=255)),
                ('skills', models.CharField(default='skill', max_length=255)),
                ('location', models.CharField(default='Dehra', max_length=50)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Eduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title1', max_length=150)),
                ('school_name', models.CharField(default='Igmp', max_length=255)),
                ('university_name', models.CharField(default='HPBS', max_length=255)),
                ('location', models.CharField(default='Dehra', max_length=50)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='static/image')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='static/image')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('heading', models.CharField(default='heading', max_length=255)),
                ('tools', models.CharField(default='tools', max_length=200)),
                ('front', models.CharField(default='HTML', max_length=255)),
                ('back', models.CharField(default='Python', max_length=255)),
                ('database', models.CharField(default='MYSQL', max_length=200)),
                ('image1', models.ImageField(null=True, upload_to='static/image')),
                ('description1', models.TextField()),
                ('image2', models.ImageField(upload_to='static/image')),
                ('description2', models.TextField()),
                ('profile', models.ImageField(upload_to='static/image')),
                ('profile_description', models.TextField()),
                ('product', models.ImageField(upload_to='static/image')),
                ('product_description', models.TextField()),
                ('product_detail', models.ImageField(upload_to='static/image')),
                ('product_detail_description', models.TextField()),
                ('cart', models.ImageField(null=True, upload_to='static/image')),
                ('cart_description', models.TextField()),
                ('wishlist', models.ImageField(null=True, upload_to='static/image')),
                ('wishlist_description', models.TextField()),
                ('duration', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=255, null=True)),
            ],
        ),
    ]
