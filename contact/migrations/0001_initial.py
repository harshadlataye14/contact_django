# Generated by Django 3.0.5 on 2020-11-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('info', models.CharField(max_length=300)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]