# Generated by Django 2.2 on 2022-06-23 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_edition', models.IntegerField(default=1)),
                ('book_author', models.CharField(max_length=20)),
                ('book_publisher', models.CharField(max_length=30)),
                ('book_copies', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('st_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('st_name', models.CharField(max_length=55)),
                ('st_family_name', models.CharField(max_length=55)),
                ('st_course', models.CharField(max_length=55)),
                ('st_undergraduate', models.BooleanField(default=True)),
                ('st_year', models.IntegerField(default=1)),
                ('st_age', models.IntegerField(default=18)),
                ('st_birthdate', models.DateTimeField(auto_now_add=True)),
                ('st_contact_number', models.IntegerField()),
                ('st_email', models.EmailField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('staff_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=15)),
                ('staff_family_name', models.CharField(max_length=15)),
                ('staff_contact', models.IntegerField()),
                ('staff_email', models.EmailField(max_length=30, unique=True)),
                ('staff_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField()),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_title', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.IntegerField(default=30)),
                ('book_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.Book')),
                ('st_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.Student')),
            ],
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_type', models.CharField(max_length=20)),
                ('book_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.Book')),
            ],
        ),
    ]
